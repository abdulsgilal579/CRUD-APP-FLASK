from flask import Flask


def create_app():
    app = Flask(__name__)
    # __name__ Represents the file name
    app.config["SECRET_KEY"] = "abdulsamad579@gmail.com"
    from .views import views
    from .auth import auth

    # This is called a relative import in Python.
    # Means: “Look for a file called views.py in the same package/folder, and import the variable/function/object named views from it”

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    return app
