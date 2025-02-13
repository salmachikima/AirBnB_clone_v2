#!/usr/bin/python3
"""
Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(_):
    """Closing the storage"""
    storage.close()



@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    """cities and states in alpha order"""
    states = storage.all(State, id)
    return render_template("9-states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
