from flask import Flask
import environment as env

def create_app():
    app = Flask(__name__)
    init_environment( app )
    init_blueprint( app ) 
    
    return app
    
def init_environment( app ):
    app.config['SECRET_KEY']                     = env.flask_secret_key
    app.config['SQLALCHEMY_DATABASE_URI']        = env.sqlalchmy_database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = env.sqlalchmy_track_modifications

    
def init_blueprint( app ):
    from controller import main_controller
    from controller import appeal_controller
    from controller import test_controller
    
    from controller import bp_main
    from controller import bp_appeal
    from controller import bp_test

    app.register_blueprint(bp_main)
    app.register_blueprint(bp_appeal)
    app.register_blueprint(bp_test)