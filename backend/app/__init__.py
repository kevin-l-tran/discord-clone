import os

from flask import Flask
from mongoengine import connect
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

flask_bcrypt = Bcrypt()

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "temporary key")

    connect(
        db=os.getenv("MONGO_DB", "my_database"),
        host=os.getenv("MONGO_HOST", "localhost"),
        port=int(os.getenv("MONGO_PORT", 27017)),
    )

    flask_bcrypt.init_app(app)

    return app
