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

@app.route('/blog/', methods=["GET","POST"])
def blog():
    posts = db.session.query(BlogPost).order_by(BlogPost.id.desc()).limit(10)
    return render_template('blog.html', posts=posts)


@app.route("/blog/<int:blog_id>/<path:blog_title>/")
def blog_post(blog_id, blog_title):
    blogpost = db.session.query(BlogPost).filter_by(id=blog_id).one()
    return render_template('blog-post.html', blogpost=blogpost)


@app.route("/blog/<int:author_id>/newpost/", methods=["GET","POST"])
def newBlogPost(author_id):
    error = None
    form = MessageForm(request.form)
    if form.validate_on_submit():
        newpost = BlogPost(title=form.title.data, description=form.description.data,author_id=current_user.id)
        db.session.add(newpost)
        db.session.commit()
        flash('your post was successful', 'success')
        return redirect(url_for('blog'))


    return render_template('create-post.html', form=form, error=error)


@app.route("/blog/<int:author_id>/<int:blog_id>/edit/", methods=["GET","POST"])
def editBlogPost(author_id, blog_id):
    error = None
    editpost = db.session.query(BlogPost).filter_by(id=blog_id).one()
    form = MessageForm(obj=editpost)
    if request.method == "GET":
        return render_template('edit-post.html', editpost=editpost, form=form, error=error)
        
    if request.method == "POST":
        editpost.title = request.form['title']
        editpost.description = request.form['description']
        db.session.add(editpost)
        db.session.commit()
        flash("Post successfully edited", "success")
        return redirect(url_for('blog'))



@app.route("/blog/<int:author_id>/<int:blog_id>/delete/")
def deleteBlogPost(author_id, blog_id):
    deletepost = db.session.query(BlogPost).filter_by(id=blog_id).one()
    return render_template('delete-post.html',deletepost=deletepost)

# route for handling the login page logic
@app.route('/login', methods=["GET", "POST"])
def login():
    error = None
    form = LoginForm(request.form)
    # if request.method == "POST":
    if form.validate_on_submit():
        user = User.query.filter_by(name=request.form['username']).first()
        if user is not None and bcrypt.check_password_hash(user.password, request.form['password']):
            login_user(user)
            flash("You were logged in. Go Crazy.", 'success')
            return redirect(url_for('index'))
        else:
            flash("Try again", "danger")
            return redirect(url_for('login'))
    return render_template("login.html", form=form, error=error)	


@app.route('/logout')
# @login_required
def logout():
    logout_user()
    session.pop('logged_in', None)
    flash('You were logged out.', 'warning')
    return redirect(url_for('blog'))

