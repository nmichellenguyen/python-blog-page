from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


db.create_all()


@app.route("/")
def hello():
    return "Hello CoderSchool!"


@app.route('/posts')
def posts():
    p = Post.query.all()
    return render_template('posts.html', posts=p)


@app.route('/create', methods=['POST', 'GET'])
def create():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))

        # access the data using request.form['field_name']
        # save it to the database
        # return a redirect to /posts
        # the code below is executed if the request method
        # was GET or the credentials were invalid
    return render_template('create.html')
