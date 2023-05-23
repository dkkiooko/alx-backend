#!/usr/bin/env python3
"""force particular locale"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """ support language list"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', strict_slashes=False, methods=['GET'])
def hello_world() -> str:
    """display simple HTML file"""
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """ get locale """
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
