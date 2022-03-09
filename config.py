class Config:
    SECRET_KEY = 'secret'

class DevConfig(Config):
    debug = True

class ProdConfig(Config):
    pass


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}