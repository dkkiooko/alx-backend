#!/usr/bin/env python3
"""basic babel setup"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """ support language list"""
    LANGUAGES = ['en', 'es']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', strict_slashes=False, methods=['GET'])
def hello_world() -> str:
    """display simple HTML file"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
