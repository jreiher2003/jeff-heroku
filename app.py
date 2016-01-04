# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
	return render_template('blog.html')

@app.route('/projects')
def project():
	return render_template('projects.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)