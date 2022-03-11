from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    # Add App Configs
    if app.config['ENV'] == 'development':
        app.config.from_object(config_options['development'])
    elif app.config['ENV'] == 'testing':
        app.config.from_object(config_options['testing'])
    else:
        app.config.from_object(config_options['production'])

    # Initialize Database
    db.init_app(app)

    # Register App Blueprints
    from .main.auth import auth
    from .main.views import views

    app.register_blueprint(views)
    app.register_blueprint(auth, url_prefix='/auth') 


    return app