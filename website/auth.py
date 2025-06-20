from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# A Blueprint is a way to organize routes and logic into reusable, modular sections of your Flask app.

auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email", "")
        fullName = request.form.get("fname", "")
        password = request.form.get("pass", "")
        confirmPassword = request.form.get("confirm_pass", "")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("You already Exit!", category="error")
        elif len(email) < 4:
            flash("Email must be longer than 4 characters.", category="error")
        elif len(fullName) < 4:
            flash("Full name must be longer than 4 characters.", category="error")
        elif password != confirmPassword:
            flash("Passwords do not match.", category="error")
        elif len(password) < 8:
            flash(
                "Password is too short. Must be at least 8 characters.",
                category="error",
            )
        else:
            new_user = User(
                email=email,
                fullName=fullName,
                password=generate_password_hash(
                    password, method="pbkdf2:sha256", salt_length=8
                ),
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account created successfully!", category="success")
            # Redirect back to signup page to clear the POST request
            return redirect(url_for("views.home"))

    return render_template("signup.html", user=current_user)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("pass")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in Successfully", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect Password", category="error")
        else:
            flash("Email does not exit!", category="error")
    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required  # this is called Decorator, This make sure we don't access this Logout Page unless we are login
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
