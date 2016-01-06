# import the Flask class from the flask module
from flask import Flask, render_template, redirect, \
    url_for, request, session, flash
from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy
import sqlite3

# create the application object
app = Flask(__name__)

# config
# import os
import os
app.config.from_object(os.environ['APP_SETTINGS'])
print os.environ['APP_SETTINGS']
# create the sqlalchemy object
db = SQLAlchemy(app)

# import db schema
from models import *

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
	posts = db.session.query(BlogPost).all()
	return render_template('blog.html', posts=posts)

@app.route('/projects')
def project():
	return render_template('projects.html')

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if (request.form['username'] != 'admin') \
                or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were logged in.')
            return redirect(url_for('blog'))
    return render_template('login.html', error=error)	


@app.route('/logout')
# @login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('blog'))



# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)