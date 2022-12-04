#!/usr/bin/python3
""" Module 8-cities_by_states """

from flask import Flask, render_template
from models.__init__ import storage


app = Flask(__name__)


app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exit):
    storage.close()


@app.route("/states/", defaults={"id": None})
@app.route("/states/<id>")
def states(id):
    from models.state import State
    from models.city import City

    st = storage.all(State)
    ci = storage.all(City)

    if id is not None:
        for state in st.values():
            if state["id"] == id:
                st = state

    return render_template("9-states.html", states=st, cities=ci, id=id)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
