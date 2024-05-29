#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    return users.get(user_id)


class Config:
    """Config class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get locale from request"""
    if "locale" in request.args:
        requested_locale = request.args["locale"]
        if requested_locale in app.config["LANGUAGES"]:
            return requested_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.before_request
def before_request():
    """Get user"""
    user_id = request.args.get("login_as")
    if user_id:
        user = get_user(int(user_id))
        g.user = user
    else:
        g.user = None


@app.route("/")
def index():
    """Display the index HTML page"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)
