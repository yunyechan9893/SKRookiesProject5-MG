from flask import Flask, request
from measure_similarity import Measure_similarity as MS
import environment as env
import logging
import json
import gpt
import datetime
import pymysql
from db_manager import DB_manager as DB;

app = Flask(__name__)


# 나중엔 지우자
stream_handler = logging.StreamHandler()
####


connection = pymysql.connect(
            host        = env.db_ip,
            port        = env.db_port,
            user        = env.db_user_id,
            password    = env.db_user_pw,
            database    = env.db_name,
            cursorclass = pymysql.cursors.DictCursor
        )



# 질문받기
@app.route('/get_sim_text', methods=["GET","POST"])
def get_sim_text():
    ms = MS()
    db = DB()
    req = request.get_json()
    
    friend_num      = req["friendNum"]
    query_data      = req["chat"][-1]
    content         = query_data["content"]
    date            = query_data["date"]
    dog_id          = req["dogId"]
    user_id         = req["userId"]
    dog_name        = req["dogName"]
    dog_age         = req["age"]
    dog_persona     = req["persona"]
    dog_species     = req["species"]
    experience      = req["experience"]
    Accent          = req["Accent"]


    # 사용자 채팅을 저장하고 저장된 No값을 가져온다
    sql = """
            INSERT INTO chat ( friend_list_no, chat_content, sent_or_received, chat_date, suitability_type, suitability ) 
            VALUES ( %s, %s, 0, %s, null, null  );
    """
    chat_date = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    args = (friend_num, content, chat_date)

    no = db.insert_commend(sql=sql, args=args)
        
    # 사용자 채팅을 임베딩한다
    embad_query   = ms.make_text_2_embading(content)
    # 사용자 채팅을 vectorDB 유사도 검사를 하여 no값을 리스트로 받아온다
    sim_text_noes = ms.measure_similar( friend_num, embad_query, ms.get_value_cnt() )
    
    # 유사도 검사 후 받은 no값으로 과거 채팅 내용을 찾아온다
    Chatting = []
    formal_chatting_str = ''
    if len(sim_text_noes):
        sql_above = '''
                    SELECT * FROM chat 
                    WHERE no < %s
                    AND friend_list_no = %s
                    ORDER BY no DESC LIMIT 5;
        '''
        args=(sim_text_noes[0], friend_num)
        Chatting.extend(db.select_commend(sql=sql_above,args=args, multy=True))

        sql_below = '''
                    SELECT * FROM chat 
                    WHERE no >= %s
                    AND friend_list_no = %s
                    ORDER BY no ASC LIMIT 5;
        '''
        args=(sim_text_noes[0], friend_num)
        Chatting.extend(db.select_commend(sql=sql_below,args=args, multy=True))


        
        # idx_name를 key로 vectorDB에 임베딩된 사용자 채팅을 저장한다
        query_sim_form = ms.make_upsert_form(idx_name=str(no),embading_text=embad_query, friend_no=friend_num)
        # ms.upsert(query_sim_form)

        # 과거 유사도 높은 채팅을 ["yc:재밌었다-2023.06.01 11:22:11", ... ] 로 만들어준다
        formal_chatting = [f'''{dog_name if int.from_bytes(chat["sent_or_received"], byteorder='little') else user_id  }:{chat["chat_content"]}-{chat["chat_date"]}\n''' for chat in Chatting]
        formal_chatting.reverse()
        formal_chatting_str = ''.join(formal_chatting)
        app.logger.info(formal_chatting_str)

    # prompt 저장소에서 prompt를 가져옴
    with open('gpt/prompt_save.json','r', encoding='utf-8') as f:
        prompt_file = json.load(f)
        dog_persona_prompt = prompt_file["prompt"][1]["content"]
        dog_answer = prompt_file["prompt"][2]["content"]

    model = gpt.init_openai()

    
    
    chat_contents = [
        {
            "role":f"{'assistant' if chat_datum['send'] else 'user'}", 
            "content" : f"chatting_content : {chat_datum['content']}, send_time : {chat_datum['date']}"
        }
        for chat_datum in req["chat"][:-1]
    ]
    now_time= datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")
    
    
    messages = [
        {
            "role": "system", 
            "content": gpt.create_personas_prompt( 
                dog_persona_prompt, 
                content, 
                dog_persona,
                user_id, 
                dog_name, 
                dog_species, 
                dog_age,
                formal_chatting_str,
                now_time,
                experience
            ) 
        }
    ]

    messages.extend(chat_contents)
    
    
    gpt.append_query_message(messages, gpt.create__prompt(dog_answer, content, Accent))



    answer = gpt.respone_awnser(model, messages)

    sql = """
            INSERT INTO chat ( friend_list_no, chat_content, sent_or_received, chat_date, suitability_type, suitability ) 
            VALUES ( %s, %s, 1, %s, null, null  );
    """
    chat_date = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    args = (friend_num, answer.replace("Answer:","").replace("Answer :","").replace("답변:","").replace("답변 :",""), chat_date)
    no = db.insert_commend(sql=sql, args=args)
    
    
    embad_query   = ms.make_text_2_embading(content)
    query_sim_form = ms.make_upsert_form(idx_name=str(no),embading_text=embad_query, friend_no=friend_num)
    # ms.upsert(query_sim_form)

    return {"answer":answer, "date":chat_date}



@app.route('/db/select', methods=["POST"])
def db_select():
    db = DB()

    req   = request.get_json()
    sql   = req["sql"].replace('\n', ' ')
    args  = tuple(req["args"])
    multy = req["multy"]
    result = db.select_commend( sql=sql, args=args, multy=multy )
    
    return {"result":result} 

@app.route('/db/insert', methods=["POST"])
def db_insert():
    db = DB()

    req   = request.get_json()
    sql   = req["sql"]
    args  = req["args"]
    result = db.select_commend( sql=sql, args=args )
    
    return {"result":result}
