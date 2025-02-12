#!/usr/bin/python3
"""Simple flask server with three end points /,  /hbnb and /c
and listens on port 5000
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displaying Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displaying HBNB again"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displaying c and the value of the next var"""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
