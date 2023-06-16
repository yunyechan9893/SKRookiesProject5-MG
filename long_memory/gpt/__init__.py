import openai
import ast
import time
import environment as env

# openai 초기화
def init_openai():
    openai.api_key = env.openai_api_key
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
def create_personas_prompt( prompt, text, persona,nickname, name, species, age, message, now_time, experience ):
    prompt = prompt.format( text=text, persona=persona, nickname=nickname, name=name,species=species,age=age, message=message, time=now_time, experience=experience )
    return prompt

# 답변 형식 프롬프트
def create__prompt( prompt, text, Accent ):
    prompt = prompt.format( text=text )
    return prompt


def get_dog_chat( model, messages ):
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    
    return response['choices'][0]['message']['content']

def respone_awnser(model, messages):
    try:
        return get_dog_chat( model, messages )
    except openai.error.RateLimitError as e:
        retry_time = e.retry_after if hasattr(e, 'retry_after') else 15
        print(f"Rate limit exceeded. Retrying in {retry_time} seconds...")
        time.sleep(retry_time)
        return get_dog_chat( model, messages )

    except openai.error.APIError as e:
        retry_time = e.retry_after if hasattr(e, 'retry_after') else 15
        print(f"API error occurred. Retrying in {retry_time} seconds...")
        time.sleep(retry_time)
        return get_dog_chat( model, messages )

    except OSError as e:
        retry_time = 5  # Adjust the retry time as needed
        print(f"Connection error occurred: {e}. Retrying in {retry_time} seconds...")      
        return get_dog_chat( model, messages )

