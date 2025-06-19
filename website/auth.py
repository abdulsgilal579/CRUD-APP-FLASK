from flask import Blueprint, render_template, request, flash, redirect, url_for

# A Blueprint is a way to organize routes and logic into reusable, modular sections of your Flask app.

auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email", "")
        fullName = request.form.get("fname", "")
        password = request.form.get("pass", "")
        confirmPassword = request.form.get("confirm_pass", "")

        if len(email) < 4:
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
            flash("Account created successfully!", category="success")
        # Redirect back to signup page to clear the POST request
        return redirect(url_for("auth.signup"))

    return render_template("signup.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    data = request.form
    print(data)
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return render_template("home.html")
