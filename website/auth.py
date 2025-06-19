from flask import Blueprint, render_template

# A Blueprint is a way to organize routes and logic into reusable, modular sections of your Flask app.

auth = Blueprint("auth", __name__)


@auth.route("/signup")
def signup():
    return render_template(
        "signup.html",
        text="Testing, You are doing great job Abdul!",
        # text here is a variable which we can access in singup template using {{text}}
    )


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return render_template("home.html")
