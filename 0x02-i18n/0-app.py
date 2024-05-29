#!/usr/bin/env python3
"""Basic Babel setup"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    """Display the index HTML page"""
    return render_template(
        "0-index.html", title="Welcome to Holberton", header="Hello world"
    )


if __name__ == "__main__":
    app.run(debug=True)
