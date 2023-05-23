#!/usr/bin/env python3
"""basic flask app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', method=['GET'], strict_slashes=False)
def hello_world() -> str:
    """display simple HTML file"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
