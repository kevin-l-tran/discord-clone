from flask import Blueprint, json, jsonify
from flask_jwt_extended import current_user, jwt_required

from . import jwt
from .models import Group, GroupMembership

groups = Blueprint("groups", __name__)


@groups.route("/groups", methods=["GET"])
@jwt_required()
def get_groups():
    memberships = GroupMembership.objects(user=current_user).select_related('group')
    groups = [json.loads(m.group.fetch().to_json()) for m in memberships]
    return jsonify(groups), 200
