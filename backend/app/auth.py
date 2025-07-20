from flask import Blueprint, request, jsonify
from mongoengine.errors import DoesNotExist, MultipleObjectsReturned
from flask_jwt_extended import create_access_token

from models import User

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
def login():
    username = request.json.get("name", None)
    password = request.json.get("password", None)

    if not username:
        return jsonify({"err": "Missing username"}), 400
    if not password:
        return jsonify({"err": "Missing password"}), 400

    try:
        user = User.objects.get(name__exact=username)
    except DoesNotExist:
        return jsonify({"err": "Bad username"}), 401
    except MultipleObjectsReturned:
        return jsonify({"err": "DB integrity broken (identical emails)"}), 500
    else:
        if not user.check_password(password):
            return jsonify({"err": "Bad password"}), 401

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200