from flask import Blueprint

# A Blueprint is a way to organize routes and logic into reusable, modular sections of your Flask app.

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return "<h1>This is the login page</h1>"


@auth.route("/logout")
def logout():
    return "<h1>This is the logout page</h1>"


@auth.route("/signup")
def signup():
    return "<h1>This is the Signup page</h1>"
