#!/usr/bin/python3
"""Starts a Flask web application.

The app liste on 0.0.0.0, port 5000.

"""
from models import storage
from flask import Flask
from flask import render_template
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def lis_states():
    """Displa an HTML page  is lis of al State obj in DBS.

    States are sort by name.
    """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def zerdown(exc):
    """Remove the current SQLA session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
