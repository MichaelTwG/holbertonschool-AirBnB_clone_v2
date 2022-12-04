#!/usr/bin/python3
""" Module 8-cities_by_states """

from flask import Flask, render_template
from models.__init__ import storage


app = Flask(__name__)


app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exit):
    storage.close()

@app.route("/cities_by_states")
def cities_by_states():
    from models.state import State
    from models.city import City

    st = storage.all(State)
    ci = storage.all(City)

    return render_template("8-cities_by_states.html", states=st, cities=ci)

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
