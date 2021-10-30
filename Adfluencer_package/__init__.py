from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
# login_manager = LoginManager(app)
# # login_manager.init_app(app)
# login_manager.login_view = 'login'

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///adfluencer.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'b8f3aabd290888870cc64c5ab34d0484'
    
    db.init_app(app)
    from Adfluencer_package.views import views
    

    
    app.register_blueprint(views, url_prefix='/')
    

    from .models import user_advt, user_infl
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'views.login'

    @login_manager.user_loader
    def load_user(id):
        return user_infl.query.get(int(id)) or user_advt.query.get(int(id))

    return app