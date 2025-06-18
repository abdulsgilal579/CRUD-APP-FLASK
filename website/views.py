from flask import Blueprint

# A Blueprint is a way to organize routes and logic into reusable, modular sections of your Flask app.

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return "<h1>This is Home Page<h2>"
