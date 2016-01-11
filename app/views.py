from app import *
from flask import render_template, redirect, \
    url_for, request, session, flash
from forms import LoginForm

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
    mistake = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            if user is not None and bcrypt.check_password_hash(user.password, request.form['password']):
                session['logged_in'] = True
                flash('You were logged in. Go Crazy')
                return redirect(url_for('blog'))
        else:
            mistake = 'Invalid Credentials. Please try again.'
    return render_template('login.html', mistake=mistake, form=form)	


@app.route('/logout')
# @login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('blog'))

