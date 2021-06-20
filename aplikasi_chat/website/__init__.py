from flask import Flask
from configs import AppEnv
from flask_sqlalchemy import SQLAlchemy
from flask_argon2 import Argon2
from flask_login import LoginManager
from flask_socketio import SocketIO

socketio = SocketIO()
db = SQLAlchemy()
argon2 = Argon2()

def create_app():
    app =  Flask(__name__)
    env = AppEnv()
    
    app.config['SECRET_KEY'] = env.SECRET_KEY()
    app.config['SQLALCHEMY_DATABASE_URI'] = env.DB_SQL_URI()
    
    db.init_app(app)
    argon2.init_app(app)
    socketio.init_app(app)

    from website.controllers.users import users
    from website.controllers.groups import groups
    from website.controllers.auth import auth
    app.register_blueprint(users,url_prefix='/users')
    app.register_blueprint(auth,url_prefix='/')
    app.register_blueprint(groups,url_prefix='/groups')
    
    from .models.user import User
    from .models.user_friend import UserFriend
    from .models.group import Group
    from .models.user_group import UserGroup

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    
    return app

def create_database(app):
    db.create_all(app=app)