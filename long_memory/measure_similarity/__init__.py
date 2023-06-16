import pinecone
from sentence_transformers import SentenceTransformer
import environment as env

class Measure_similarity:
    def __init__( self ) -> None:
        self.model = SentenceTransformer( env.embading_model )
        pinecone.init( api_key=env.pinecone_api_key, environment=env.resion )
        self.table_name = pinecone.list_indexes()

        if not self.table_name :
                metadata_config = {
                    "indexed": ["friend_no"]
                }

                pinecone.create_index(
                    "quickstart", 
                    dimension=768, 
                    metric="cosine",
                    metadata_config=metadata_config
                )
                self.table_name = pinecone.list_indexes()

        self.index = pinecone.Index(self.table_name[0])


    def make_text_2_embading( self, conversation ):
        return self.model.encode(conversation).tolist()


    def make_upsert_form(self, idx_name, embading_text, friend_no ):
        return [(f'{idx_name}', embading_text,{"friend_no": friend_no})]


    def measure_similar( self, friend_no, embading_text, val_cnt, top_k=1 ):
        if val_cnt :
            try:
                score = self.index.query(
                    vector=embading_text,
                    top_k=top_k,
                    include_values=True,
                    filter={
                        "friend_no": friend_no
                    }
                )

                return [int(s['id']) for s in score['matches']] 
            except Exception as e:
                return []

        return []
    
    def get_value_cnt(self):
        return self.index.describe_index_stats()['namespaces']
        
    def upsert( self, upsert_form_text ) :
        self.index.upsert( upsert_form_text )

    

    