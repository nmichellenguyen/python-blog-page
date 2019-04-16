Python- Flask Intro- Solo Project

### Milestone 1: Get Started

Create a new application, and create a new file. You can call it whatever you like; why not `blog.py`?

Create your main routes. For now, it's okay to have everything in one file as our app will stay simple.

The routes you'll need are:

- The default base route. This should return a redirect to `/posts`. \*[Flask Documentation on how to Redirect](http://flask.pocoo.org/docs/1.0/quickstart/#redirects-and-errors)
- A `/posts` route to show all the posts.
- A `/create` route that shows a form to create a new post.

### Milestone 2: Create your Models

For this application, we'll keep things simple and not have a real user authentication system; we only need one table for now.

Define your model for `Post`. It should have a few fields:

- id (always)
- title
- body
- author_name
- created_at
- updated_at

Those last two models, you'll be able to use a nice feature of SQLAlchemy: https://stackoverflow.com/a/12155686/396324. As you use SQLALchemy more and more, you'll start to like it more.

Remember to make the title and body required, and have some minimum length. A great way to do this in SQLAlchemy is to use the [@validates decorator](https://stackoverflow.com/a/18579864/396324).

You do the above _in addition_ to defining `NOT NULL`, as in the [simple example from the docs](https://flask-sqlalchemy.readthedocs.io/en/stable/models/#simple-example). `nullable=False` enforces this at the database level - `@validates` works at the Python level.

### Milestone 3: Create your first form

The most common framework is Flask-WTF, but we'll learn that later. What's nice about Flask is we can build simple solutions first.

We'll just use `request.form`. There's an article linked above in the resources that has a longer introduction, but for now the code sample [at the official docs](http://flask.pocoo.org/docs/1.0/quickstart/#the-request-object) should have everything you need.

First though let's create the actual form. Create a new route, called `/create`, that renders a template for a form (something like `render_template('create_form.html'`).

After you have created your form, let's write the more interesting part: the handler.

At the top of your code, make sure to import:

```
from flask import request
```

We can actually process the creation into the same handler that displays the form - we can use `GET` and `POST` to differentiate between showing the form or processing the form. It's common practice to do this, but you can definitely create different endpoints if you wish.

```
@app.route('/create', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        # access the data using request.form['field_name']
        # save it to the database
        # return a redirect to /posts
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('create_form.html')
```

### Milestone 4: Add Bootstrap and some Styling

To do this, we'll have to use template inheritance. Your pages probably don't have a nice head, body, and consistent style, nav bar, footer, that sort of stuff that you're probably used to.

[Flask Documentation](http://flask.pocoo.org/docs/1.0/patterns/templateinheritance/) is great here.

Two steps:

1. Create a file called `layout.html`, with named "blocks" for the children to fill in.
2. Child templates all call `{% extends "layout.html" %}`.

### Milestone 5: Flash Messages / Error Feedback

We redirect to posts right away when we create a new post, whether it was successful or not.

Two things to change:

1. Only redirect to `/posts` if the model creation was successful. Else, redirect back to `/create`.
2. Show a `flash` message explaining what happened.

[http://flask.pocoo.org/docs/1.0/patterns/flashing/](Flask documentation) is great here again. On the backend side, all you have to do is create a line that says something like `flash('Post created')`.

If there was an error, just call `flash('Error during model creation')`.
