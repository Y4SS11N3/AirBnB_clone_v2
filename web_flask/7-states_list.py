#!/usr/bin/python3

"""Start web Flask application"""

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """Display 'Hello HBNB!'"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def about_hbnb():
    """Display 'HBNB'"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def fun_c(text):
    """Display the message passed when /c is called"""
    return "C " + text.replace("_", " ")

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Display the message passed when /python is called"""
    return "Python " + text.replace("_", " ")

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Display 'n is a number' only if n is an integer"""
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def n(n):
    """Display a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    """Display a HTML page only if n is an integer"""
    return render_template("6-number_odd_or_even.html", n=n)

@app.route("/states_list", strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all State objects"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)

@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
