import os
import secret_key

# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = secret_key.secret_key
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    print SQLALCHEMY_DATABASE_URI
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False