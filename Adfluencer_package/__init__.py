from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path
from werkzeug.utils import secure_filename

db = SQLAlchemy()

DB_NAME = 'adfluencer.db'
UPLOAD_FOLDER = 'static/uploads/'

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'b8f3aabd290888870cc64c5ab34d0484'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    db.init_app(app)
    from Adfluencer_package.views import views
    
    app.register_blueprint(views, url_prefix='/')

    from .models import users, advertisements
    
    create_database(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'views.login'

    @login_manager.user_loader
    def load_user(id):
        return users.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('Adfluencer_package/' + DB_NAME):
        db.create_all(app=app)
        print('Database created!')