import os
from secret_key import secret_key


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = secret_key
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False