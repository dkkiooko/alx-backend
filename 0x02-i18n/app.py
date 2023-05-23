#!/usr/bin/env python3
"""use user locale"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union
from pytz import timezone
import pytz.exceptions


app = Flask(__name__, template_folder='templates')
babel = Babel(app)


# mock login system
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ support language list"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', strict_slashes=False, methods=['GET'])
def hello_world() -> str:
    """display simple HTML file"""
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """ get function to get the local selector """
    locale = request.args.get('locale', None)
    if locale and locale in Config.LANGUAGES:
        return locale
    if g.user:
        locale = g.user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    locale = request.headers.get('locale', None)
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """user time zone finder"""
    tzone = request.args.get('timezone', None)
    if tzone:
        try:
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return 'UTC'
    if g.user:
        try:
            tzone = g.user.get('timezone')
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return 'UTC'
    default = app.config['BABEL_DEFAULT_TIMEZONE']
    return request.accept_languages.best_match(default)


def get_user() -> Union[dict, None]:
    """ returns user dictionary """
    user_id = request.args.get('login_as', None)
    if user_id is None:
        return None
    return users.get(int(user_id))


@app.before_request
def before_request():
    """ executed before all other methods """
    usr = get_user()
    g.user = usr


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
