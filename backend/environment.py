with open('environment.env', 'r' ) as file :
    env = file.read().split('\n')
    db_user_id       = env[0].split(":")[1]
    db_user_pw       = env[1].split(":")[1]
    db_ip            = env[2].split(":")[1]
    db_port          = int(env[3].split(":")[1])
    db_name          = env[4].split(":")[1]
    flask_secret_key = env[5].split(":")[1]
    long_memory_ip   = env[6].split(":")[1]
    
    sqlalchmy_track_modifications=False
    sqlalchmy_database_uri = f'mysql+pymysql://{db_user_id}:{db_user_pw}@{db_ip}:{db_port}/{db_name}'
    