from flask import render_template, request, jsonify, redirect, url_for,current_app as app
from controller import bp_appeal as appeal
import json
import jwt
import logging
import requests
import pymysql
import environment as env
from pymysqlpool.pool import Pool

def tool(msg, form=''):
    ###
    # 로깅 레벨 설정
    app.logger.setLevel(logging.DEBUG)

    # 로깅 핸들러 추가
    stream_handler = logging.StreamHandler()

    app.logger.info("======================")
    app.logger.info(form)
    app.logger.info(msg)




def db_connection():
    pool = Pool(
        host        = env.db_ip,
        port        = env.db_port,
        user        = env.db_user_id,
        password    = env.db_user_pw,
        database    = env.db_name,
    )
    pool.init()
    return pool


def db_sql( pool, sql, args, multy=False ):
    connection = pool.get_conn()
    cur = connection.cursor()

    #트라이캐치 붙히기
    # args는 튜플로 구성
    cur.execute(sql, args=args)

    
    if multy : 
        result = cur.fetchall()
        pool.release(connection)
        return result
    else     : 
        result = cur.fetchone()
        pool.release(connection)
        return result

def db_connection2():
    return pymysql.connect(
            host        = env.db_ip,
            port        = env.db_port,
            user        = env.db_user_id,
            password    = env.db_user_pw,
            database    = env.db_name,
            cursorclass = pymysql.cursors.DictCursor
        )



@appeal.route("/answer", methods=["POST"]) 
def answer():
    user_msg = json.loads(request.data.decode('utf-8'))
    user_id = user_msg['userId']
    dog_id = user_msg['dogId']
    
    try:
        with db_connection2().cursor() as cursor:
            sql = f"""
                SELECT animal_name, age, personality, species
                FROM abandoned_animal
                WHERE animal_id='{dog_id}'
            """
            dog=dict()

            cursor.execute(sql)
            dog = cursor.fetchall()[0]
 
            sql = f"""
                SELECT experience
                FROM persona
                WHERE animal_id='{dog_id}'
            """
            dog2=dict()

            cursor.execute(sql)
            dog2 = cursor.fetchall()[0]

            sql = f"""
                SELECT Accent
                FROM dog_Accent
                WHERE animal_id='{dog_id}'
            """

            cursor.execute(sql)
            dog3 = cursor.fetchall()[0]

    except Exception as e:
        pass
    finally:
        cursor.close()
        
        user_msg["dogName"] = dog.get("animal_name")
        user_msg["age"]     = dog.get("age")
        user_msg["persona"] = dog.get("personality")
        user_msg["species"] = dog.get("species")
        user_msg["experience"] = dog2.get("experience")
        user_msg["Accent"] = dog3.get("Accent")
        app.logger.info(user_msg["Accent"])
        


    # GPT 프롬프트 엔지니어링 부분 모듈 로드
    url = f'http://{env.long_memory_ip}:3333/get_sim_text'
    headers = {'Content-Type': 'application/json'}
    resp = requests.post(url, data=json.dumps(user_msg), headers=headers).json()
    message = {                       # 주고받는 메세지의 속성값을 저장한다
        'message_type'    : 'bot', 
        'dog_name'        : dog["animal_name"],
        'message_content' : resp["answer"],
        'time'            : resp["date"]
    }
    app.logger.info(message["message_content"])
    if 'Answer' in message["message_content"]:
        update_dic ={"message_content" : message["message_content"].replace('Answer', '').replace(':', '')}
        message.update(update_dic)
    else:
        pass

    return jsonify(message) # message 안에는 (messsagetype(사용자인지,봇인지 판단), 강아지 이름, 강아지 채팅 내용, 시간) 으로 이루어져있다.

# 채팅 페이지
@appeal.route("/load_chat_page", methods=["GET", "POST"])
def load_chat_page():
    dog_info  = json.loads(request.args.get('dog_id').replace("'",'"'))
    dog_id    = dog_info.get('dog_id')
    friend_no = dog_info.get('friend_no')
    
    # jwt에서 받아올 예정
    user_id = 'yc'

    try:
        with db_connection2().cursor() as cursor:
            sql = f"""
                SELECT animal_name, diffusion_profile_image
                FROM abandoned_animal 
                WHERE animal_id = '{dog_id}' 
            """
            cursor.execute(sql)
            dog_info = cursor.fetchall()[0]

    except Exception as e:
        pass
    finally:
        cursor.close()

    
    dog_info_json = {
        "dog_id"    : dog_id, 
        "dog_name"  : dog_info.get("animal_name"), 
        "img_src"   : dog_info.get("diffusion_profile_image"), 
        "user_id"   : user_id,
        "friend_no" : friend_no.get("no")
    }

    return render_template("chat.html", dog_info=dog_info_json)
    

    


@appeal.route("/load_before_chat", methods=["POST"])
def load_before_chat():
    dog_info  = json.loads(request.data.decode('utf-8'))
    friend_number = dog_info.get("friendNo")
    dog_id  = dog_info.get("dogId")
    user_id = dog_info.get("userId")


    sql = """
            SELECT chat_content, sent_or_received, chat_date
            FROM chat
            WHERE friend_list_no = %s
            ORDER BY no DESC
            limit 10;
    """
    
    args = (friend_number,)
    chat_info = db_sql(pool=db_connection(),sql=sql,args=args,multy=True)
    
    
    chat_contents = [{ "no":idx, "content": chat["chat_content"],"send":int.from_bytes( chat["sent_or_received"] ), "date":str(chat["chat_date"]) } for idx, chat in enumerate(chat_info)]
    current_chat_list = {
            "user_id" : dog_id,
            "dog_id"  : user_id,
            "friend_list_no" : friend_number,
            "chat": chat_contents
        }

    return current_chat_list


@appeal.route('/mgti_start', methods=['GET', 'POST'])
def mgti_start():
    return render_template("mgti_start.html")

# MGTI 진행 페이지


@appeal.route('/mgti_ing', methods=['GET', 'POST'])
def mgti_ing():
    return render_template("mgti_ing.html")


@appeal.route('/mgti_res', methods=['get', 'post'])
def res2():
    data = json.loads(request.form.get('result'))
    score = [0] * 4

    for mbti_form, val in data.values():
        score[mbti_form] += val

    mbti = [["I", "E"], ["N", "S"], ["T", "F"], ["J", "P"]]
    dog_mbti = {"mbti":"".join(mbti[idx][each_score < 0] for idx, each_score in enumerate(score))}
 
    return render_template('mgti_res.html', mbti=dog_mbti)

@appeal.route('/mgti_res/get_dog', methods=['get', 'post'])
def get_dog():
    mbti = request.data.decode('utf-8')

    try:
        with db_connection2().cursor() as cursor:
            sql = f'''
                SELECT animal_id, diffusion_profile_image
                FROM abandoned_animal
                WHERE mbti_type='{mbti}'
                LIMIT 4;
            '''

            cursor.execute(sql)
            dog = {"dogs":cursor.fetchall()}


            sql = f'''
                SELECT mbti_introduction
                FROM species_for_mbti
                WHERE mbti_type='{mbti}'
            '''

            cursor.execute(sql)
            dog["mbti_info"] = cursor.fetchone()["mbti_introduction"]

    except Exception as e:
        pass
    finally:
        cursor.close()

    return dog
