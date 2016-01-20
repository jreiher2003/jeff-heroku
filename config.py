import os
import secret_key

# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = secret_key.secret_key
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    POSTS_PER_PAGE = 10
    print SQLALCHEMY_DATABASE_URI
   


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False