from flask import Flask
from config import config_options

def create_app(config_name):

    app = Flask(__name__)

    # Add App Configs
    app.config.from_object(config_options[config_name])

    # Register App Blueprints
    from .main.auth import auth
    from .main.views import views

    app.register_blueprint(views)
    app.register_blueprint(auth, url_prefix='/auth') 


    return app