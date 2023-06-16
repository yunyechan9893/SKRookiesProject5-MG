from pymysqlpool.pool import Pool
import environment as env

class DB_manager :
    def __init__(self):
        self.pool = Pool(
            host        = env.db_ip,
            port        = env.db_port,
            user        = env.db_user_id,
            password    = env.db_user_pw,
            database    = env.db_name,
        )
        
        self.pool.init()


    
    def select_commend( self, sql, args, multy=False ):       
        connection = self.pool.get_conn()
        cur =  connection.cursor()
        #트라이캐치 붙히기
        # args는 튜플로 구성
        cur.execute(sql, args=args)

        result= cur.fetchall() if multy else cur.fetchone()
        self.pool.release(connection)
        return result
    
    def insert_commend( self, sql, args ):       
        connection = self.pool.get_conn()
        cur =  connection.cursor()
    
        #트라이캐치 붙히기
        # args는 튜플로 구성
        cur.execute(sql, args=args)
        connection.commit()
        cur.execute("SELECT LAST_INSERT_ID();")
        _, result = next(iter(cur.fetchone().items()))
        self.pool.release(connection)

        return result