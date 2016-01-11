from flask import Flask 
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt 
app = Flask(__name__)
import os
app.config.from_object(os.environ['APP_SETTINGS'])
print os.environ['APP_SETTINGS']
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from app import views
from models import *