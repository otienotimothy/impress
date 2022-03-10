


class Config:
    SECRET_KEY = '39a73536c3a5f91b2af5dc868c6bc5bcda54cc76a672479dcfb5372e8de687f5'

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    pass


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}