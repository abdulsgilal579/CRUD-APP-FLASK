from flask import Blueprint, render_template

# A Blueprint is a way to organize routes and logic into reusable, modular sections of your Flask app.

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")
