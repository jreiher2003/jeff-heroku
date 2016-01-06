import os
# from secret_key import secret_key


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "\x1d\xd6\xf4\x9c\xfe\xd9\xf9\x7f\x1e\xa6S=\xf0{\xf3\xb5bq4\xb8\x9b\xd65"
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False