import os
# from secret_key import secret_key
import secret_key

# default config
class BaseConfig(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = secret_key.secret_key
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    # print SQLALCHEMY_DATABASE_URI
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False