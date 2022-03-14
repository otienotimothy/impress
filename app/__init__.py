import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import config_options

db = SQLAlchemy()
migrate = Migrate()

def create_app():

    app = Flask(__name__)

    # Add App Configs
    if app.config['ENV'] == 'development':
        app.config.from_object(config_options['development'])
    elif app.config['ENV'] == 'testing':
        app.config.from_object(config_options['testing'])
    else:
        app.config.from_object(config_options['production'])
        app.config['SECRET_KEY'] = '39a73536c3a5f91b2af5dc868c6bc5bcda54cc76a672479dcfb5372e8de687f5'
        URI = os.environ.get('DATABASE_URL')
        if URI.startswith('postgres://'):
            URI = URI.replace('postgres://', 'postgresql://', 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = URI
        

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize Database
    db.init_app(app)


    # Register App Blueprints
    from .main.auth import auth
    from .main.views import views

    app.register_blueprint(views)
    app.register_blueprint(auth, url_prefix='/auth') 

    from .models import User
    migrate.init_app(app, db)

    # Authenticate User
    login_manager = LoginManager()
    login_manager.init_app(app)

    # Load User Session
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app