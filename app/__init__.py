from flask import Flask 
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt 
app = Flask(__name__)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from app import views
from models import *