#!/usr/bin/python3

"""
Simple flask server with two end points
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """
    display of hbnb
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """
    display HBNB
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
