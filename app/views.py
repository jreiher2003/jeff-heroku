from app import app, db
from flask import render_template, redirect, \
    url_for, request, session, flash
from flask.ext.login import login_user, logout_user, login_required, current_user
from forms import LoginForm, MessageForm

from app.models import User, BlogPost, bcrypt

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/blog', methods=["GET","POST"])
def blog():
    error = None
    form = MessageForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_post = BlogPost(form.title.data,form.description.data,current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash('New Post was successfully posted.', 'bg-success')
            return redirect(url_for('blog'))
    else:
    	posts = db.session.query(BlogPost).all()
    	return render_template('blog.html', posts=posts, form=form, error=error)

@app.route('/projects')
def project():
	return render_template('projects.html')

# route for handling the login page logic
@app.route('/login', methods=["GET", "POST"])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            if user is not None and bcrypt.check_password_hash(user.password, request.form['password']):
                login_user(user)
                flash("You were logged in. Go Crazy.", 'bg-success')
                return redirect(url_for('index'))
            else:
                flash("Try again", "bg-danger")
                return redirect(url_for('login'))
    return render_template("login.html", form=form, error=error)	


@app.route('/logout')
# @login_required
def logout():
    logout_user()
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('blog'))

