from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    # __name__ Represents the file name
    app.config["SECRET_KEY"] = "abdulsamad579@gmail.com"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views
    from .auth import auth

    # This is called a relative import in Python.
    # Means: “Look for a file called views.py in the same package/folder, and import the variable/function/object named views from it”

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = (
        "auth.login"  # This tells where do we go if we are not login
    )
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    db_path = path.join(app.root_path, DB_NAME)
    if not path.exists(db_path):
        with app.app_context():
            db.create_all()
        print("Database Created")
