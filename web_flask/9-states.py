#!/usr/bin/python3
"""
A script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
    Display a HTML page with a list of all State objects
    present in DBStorage sorted by name.
    """
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state(id):
    """
    Display a HTML page with info about <id>, if it exists.
    """
    state = storage.get(State, id)
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove the current SQLAlchemy session after each request.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
