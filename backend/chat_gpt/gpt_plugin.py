import openai
import ast
import json
import logging
import time

# openai 초기화
def init_openai():
    with open('chat_gpt/api_key.text', 'r', encoding='utf8') as f:
        api_key = f.read()
    openai.api_key = api_key
    model = "gpt-3.5-turbo"

    return model

# 메세지 초기화
def create_message( prompt ):
    return [
        {"role": "system", "content": prompt}
        ]

# 대화 user 메세지 append
def append_query_message( message, query ):
    message.append({"role": "user", "content": query})

# 대화 assistant 메세지 append
def append_answer_message( message, answer ):
    message.append({"role": "assistant", "content": answer})

# 대화 system 메세지 append
def append_system_message( message, answer ):
    message.append({"role": "system", "content": answer})

# 처음 메세지 user, assistant 메세지 삭제
# 일정 토큰 이상일 때 동작
def del_message(messages, idx=2):
    del messages[idx]
    del messages[idx]

    return messages


# 페르소나 프롬프트
def create_personas_prompt( prompt, text, persona,nickname, name, species, age ):
    prompt = prompt.format( text=text, persona=persona, nickname=nickname, name=name,species=species,age=age )
    return prompt

def create__prompt( prompt, text ):
    prompt = prompt.format( text=text )
    return prompt


# 과거 진위 판별 함수
def make_distinguish_chat( model, messages ):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.5,
        max_tokens=30,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=[":"]
    )

    print(response['usage']['total_tokens'])
    answer = response['choices'][0]['message']['content']
    print(answer)
    if answer[0] == "{'" and answer[-1] == "}" :
        return ast.literal_eval(answer)
    return ['x']


# API 호출, 강아지와 대화
def create_chat_dog( model, messages ):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    return response

# 대화내용 요약 ( 현재 미사용 )
def create_chat_summary( model, messages ):
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    

    return response['choices'][0]['message']['content']


def gpt( chat_data, app ):
    app.logger.setLevel(logging.DEBUG)

    # 로깅 핸들러 추가
    stream_handler = logging.StreamHandler()

    user_id = chat_data["userId"]
    query = chat_data["chat"][-1]["content"]

    dog_name = "뽀또"

    # 추후에 들어올 강아지 정보
    dog_info = {'persona':'우주비행사','nickname':'예찬','name':dog_name, 'species':'말티즈','age':'3'}

    
    # {"role": "user", "content": query}
    
    
    # prompt 저장소에서 prompt를 가져옴
    with open('chat_gpt/prompt_save.json','r', encoding='utf-8') as f:
        prompt_file = json.load(f)
        prompt = prompt_file["prompt"][0]["content"]
        dog_persona_prompt = prompt_file["prompt"][1]["content"]
        dog_answer = prompt_file["prompt"][2]["content"]

    
    model = init_openai()


    chat_contents = [
        {"role":f"{'assistant' if chat_datum['send'] else 'user'}", "content" : f"chatting_content : {chat_datum['content']}, send_time : {chat_datum['date']}"}
        for chat_datum in chat_data["chat"][:-1]
        ]

    messages = [{"role": "system", "content": create_personas_prompt( dog_persona_prompt, query, dog_info['persona'],dog_info['nickname'], dog_info['name'] , dog_info['species'], dog_info['age'] ) }]
    messages.extend(chat_contents)
    
    
    append_query_message(messages, create__prompt(dog_answer, query))

    try:
        answer = create_chat_summary( model, messages )
    except openai.error.RateLimitError as e:
        retry_time = e.retry_after if hasattr(e, 'retry_after') else 15
        print(f"Rate limit exceeded. Retrying in {retry_time} seconds...")
        time.sleep(retry_time)
        answer = create_chat_summary( model, messages )

    except openai.error.APIError as e:
        retry_time = e.retry_after if hasattr(e, 'retry_after') else 15
        print(f"API error occurred. Retrying in {retry_time} seconds...")
        time.sleep(retry_time)
        answer = create_chat_summary( model, messages )

    except OSError as e:
        retry_time = 5  # Adjust the retry time as needed
        print(f"Connection error occurred: {e}. Retrying in {retry_time} seconds...")      
        answer = create_chat_summary( model, messages )
        
    answer.replace("\n", "")

    return answer
