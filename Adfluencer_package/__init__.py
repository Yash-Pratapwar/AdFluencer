from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path
from werkzeug.utils import secure_filename

db = SQLAlchemy()

# DB_NAME = 'adfluencer.db'
UPLOAD_FOLDER = 'static/uploads/'

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://yash:1234@localhost/adfluencer' #Keep the database name as 'adfluencer' only to make our life easy, edit this according to your username and password
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://yash:1234@localhost/adfluencer' #use this line to edit and comment out the above line
    #please refer this website: https://towardsdatascience.com/sending-data-from-a-flask-app-to-postgresql-database-889304964bf2
    '''
    engine:[//[user[:password]@][host]/[dbname]]engine -> postgresql
    user -> postgres (see `owner` field in previous screenshot)
    password -> password (my db password is the string, `password`)
    host -> localhost (because we are running locally on out machine)
    dbname -> flasksql (this is the name I gave to the db in the previous step)
    '''
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'b8f3aabd290888870cc64c5ab34d0484'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    db.init_app(app)
    from Adfluencer_package.views import views
    
    app.register_blueprint(views, url_prefix='/')

    from .models import users, advertisements
    
    # create_database(app) #uncomment this line to create schema

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'views.login'

    @login_manager.user_loader
    def load_user(id):
        return users.query.get(int(id))
    return app

def create_database(app):
    # if not path.exists('Adfluencer_package/' + DB_NAME):
    db.create_all(app=app)
    print('Database created!')