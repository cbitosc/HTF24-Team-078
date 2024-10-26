from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_migrate import  Migrate


db=SQLAlchemy()
db_name="database.db"

def create_app():
    app=Flask(__name__)
    app.config["SECRET_KEY"]="DWJABKDUBAKUBSD"
    app.config["SQLALCHEMY_DATABASE_URI"]=f"sqlite:///{db_name}"

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(views, url_prefix="/")

    from .models import Doc,Patient
    create_database(app)


    return app

def create_database(appx):
    with  appx.app_context():
        if not path.exists(f"website/{db_name}"):
            db.create_all()
            print("Created Database!")
