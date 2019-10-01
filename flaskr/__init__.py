import os

from flask import Flask, redirect

import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/thomas')
    def thomas():
        redirect('https:kosciuch.ca/catfacts')

    from . import auth
    app.register_blueprint(auth.bp)

    from . import db
    db.init_app(app)

    from . import blog
    app.register_blueprint(blog.bp)
    #app.add_url_rule('/', endpoint='index')

    from . import spammer
    app.register_blueprint(spammer.bp)
    app.add_url_rule('/', endpoint='spammer/index')

    return app

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)