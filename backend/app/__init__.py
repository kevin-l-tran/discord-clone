import os
import datetime

from flask import Flask
from mongoengine import connect
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

flask_bcrypt = Bcrypt()
jwt = JWTManager()

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "temporary key")

    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "temporary key")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(hours=1)

    connect(
        db=os.getenv("MONGO_DB", "my_database"),
        host=os.getenv("MONGO_HOST", "localhost"),
        port=int(os.getenv("MONGO_PORT", 27017)),
    )

    flask_bcrypt.init_app(app)
    jwt.init_app(app)

    return app
