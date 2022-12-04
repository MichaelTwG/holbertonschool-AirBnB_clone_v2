#!/usr/bin/python3
""" Module 7-states_list """

from flask import Flask, render_template
from markupsafe import escape
from models import storage


app = Flask(__name__)

# SET STRICT SLASHES FOT ALL ROUTES
app.url_map.strict_slashes = False
# Add app.teardown_appcontxt - call storage.clos after each request
@app.teardown_appcontext
def teardown(exit):
    storage.close()


@app.route("/states_list")
def show_states_list():
    from models.state import State
    return render_template("7-states_list.html", states=storage.all(State))


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
