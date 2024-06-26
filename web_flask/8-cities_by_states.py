#!/usr/bin/python3
"""Starts a Flask web application."""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """Close the open storage engine."""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """Return a page of all `Cities` grouped by `State`, sorted."""
    states = [state for state in storage.all(State).values()]
    return render_template('8-cities_by_states.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
