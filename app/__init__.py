from flask import Flask
from config import config_options

def create_app():

    app = Flask(__name__)

    # Add App Configs
    if app.config['ENV'] == 'development':
        app.config.from_object(config_options['development'])
    elif app.config['ENV'] == 'testing':
        app.config.from_object(config_options['testing'])
    else:
        app.config.from_object(config_options['production'])

    # Register App Blueprints
    from .main.auth import auth
    from .main.views import views

    app.register_blueprint(views)
    app.register_blueprint(auth, url_prefix='/auth') 


    return app