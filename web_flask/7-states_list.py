#!/usr/bin/python3

"""Starts a Flask web application.

The app listens on 0.0.0.0, port 5000.
"""

from models import storage
from flask import Flask
from flask import render_template
from models.state import State

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def list_states():
    """Display an HTML page with a list of all State objects in DBStorage.

    States are sorted by name.
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)

@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
