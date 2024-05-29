#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template, request
from flask_babel import Babel


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


@app.route("/")
def index():
    """Display the index HTML page"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
