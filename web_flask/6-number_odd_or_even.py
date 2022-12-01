#!/usr/bin/python3
""" Module 5-hbnb_route """

from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    return "C {}".format(escape(text.replace("_", " ")))


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>")
def python(text):
    return "Python {}".format(escape(text.replace("_", " ")))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    if (n % 2) == 1:
        text = "Number: {} is odd".format(n)
    else:
        text = "Number: {} is even".format(n)
    return render_template("6-number_odd_or_even.html", text=text)

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
