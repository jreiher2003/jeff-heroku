import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'my precious'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False