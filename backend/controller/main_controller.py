from flask import render_template, request, redirect, url_for, current_app as app
from controller import bp_main as main
import pymysql
import logging
import environment as env

def connection():
    return pymysql.connect(
        host        = env.db_ip,
        port        = env.db_port,
        user        = env.db_user_id,
        password    = env.db_user_pw,
        database    = env.db_name,
        cursorclass = pymysql.cursors.DictCursor
    )

def tool(msg, text=''):
    ###
    # 로깅 레벨 설정
    app.logger.setLevel(logging.DEBUG)

    # 로깅 핸들러 추가
    stream_handler = logging.StreamHandler()

    app.logger.info("======================")
    app.logger.info(text)
    app.logger.info(msg)


# 메인페이지
@main.route('/mainpage', methods=['get','post'])
def mainpage():
    try:
        with connection().cursor() as cursor:
                sql = f'''
                    SELECT animal_id, animal_name, age, diffusion_profile_image
                    FROM abandoned_animal
                    ORDER BY increased_friends DESC
                    LIMIT 3;
                '''
                cursor.execute(sql)
                dogs = cursor.fetchall()
                
                dogs_json = {
                    "dog":dogs
                }
        
    finally:
        cursor.close()
    return render_template( 'mainpage.html' , dogs=dogs_json)


# 소개페이지
@main.route('/introduction/<dog_id>', methods=['get','post'])
def introduction(dog_id):
    user_id = 'yc'
    if request.method == 'GET':
        try:
            with connection().cursor() as cursor:
                sql = f"""
                    SELECT a.animal_name, a.age, a.introduction, a.diffusion_profile_image, p.persona
                    FROM abandoned_animal AS a
                    JOIN persona AS p ON a.animal_id = p.animal_id
                    WHERE a.animal_id = '{dog_id}'
                """
                cursor.execute(sql)
                dog_info = cursor.fetchone()
                if dog_info : dog_info["dog_id"] = dog_id
        except Exception as e:
            pass
        finally:
            cursor.close()
            
        return render_template( 'introduction.html' , dog_info=dog_info)
    else :
        try:
            conn = connection()
            with conn.cursor() as cursor:
                sql = f"""
                    SELECT no
                    FROM friend_list
                    WHERE user_id = '{user_id}'
                    AND animal_id = '{dog_id}'
                """
                friend_no=dict()
                
                cursor.execute(sql)
                friend_no = cursor.fetchone()
                friend_no = friend_no if friend_no != None else {}

                if not friend_no.get("no") : 
                    sql = f"""
                        INSERT INTO friend_list(user_id, animal_id)
                        VALUES ('{user_id}','{dog_id}')
                    """

                    cursor.execute(sql)
                    conn.commit()
            
                
                    sql = f"""
                        SELECT no
                        FROM friend_list
                        WHERE user_id = '{user_id}'
                        AND animal_id = '{dog_id}'
                    """
                    friend_no = {}
                    
                    cursor.execute(sql)
                    friend_no = cursor.fetchone()
                    friend_no = friend_no if friend_no != None else {}
        except Exception as e:
            pass
        finally:
            cursor.close()
     
    return redirect(url_for('appeal_bp.load_chat_page', dog_id={"dog_id":dog_id, "friend_no":friend_no}))
    
    
@main.route('/aboutus', methods=['get','post'])
def aboutus():
    return render_template( 'aboutus.html')

# 삭제예정
@main.route('/index', methods=['get','post'])
def index():
    return render_template( 'index.html')


@main.route('/munglist', methods=['get','post'])
def munglist():
    try:
        with connection().cursor() as cursor:
                sql = f'''
                    SELECT animal_id, animal_name, age, diffusion_profile_image
                    FROM abandoned_animal
                    ORDER BY increased_friends DESC
                    LIMIT 10;
                '''
                cursor.execute(sql)
                dogs = cursor.fetchall()
                
                dogs_json = {
                    "dog":dogs
                }
    except Exception as e:
            pass
    finally:
        cursor.close()

    return render_template( 'munglist.html' , dogs=dogs_json)

@main.route('/instruct', methods=['get','post'])
def instruct():
     return render_template('instruct.html')