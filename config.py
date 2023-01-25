class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # отслеживает изменения в базе
    DEBUG = False


class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///order.db'
    SQLALCHEMY_ECHO = True
    JSON_AS_ASCII = False
    DEBUG = True


class ProdConfig(BaseConfig):
    pass
