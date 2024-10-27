from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import  Migrate
from flask_login import LoginManager



db=SQLAlchemy()
db_name="database.db"

def create_app():
    app=Flask(__name__)
    app.config["SECRET_KEY"]="superSecretKey"
    app.config["SQLALCHEMY_DATABASE_URI"]=f"sqlite:///{db_name}"
    app.config["SESSION_TYPE"]="filesystem"

    db.init_app(app)

    

    from .views import views
    from .auth import auth

    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(views, url_prefix="/")

    from .models import Doc,Patient
    create_database(app)

    login_manager= LoginManager()
    login_manager.login_view= "auth.patient_login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Patient.query.get(int(id))

    return app

def create_database(appx):
    with  appx.app_context():
        if not os.path.exists(f"website/{db_name}"):
            db.create_all()
            print("Created Database!")
