from app.api import bp
from dataclasses import dataclass
from flask import jsonify
from app.models import User
from flask import jsonify, request, url_for, abort
from app import db
from app.api.auth import token_auth
from app.api.errors import bad_request

@bp.route("/login", methods=["PUT"])
def login():
    data = request.get_json() or {}
    if "username" not in data or "password" not in data:
        return bad_request("must include username and password fields")
    user = User.query.filter_by(username=data['username']).first()
    if user is None:
        user = User.query.filter_by(email=data['username']).first()
    if user is None:
        user = User.query.filter_by(id=data['username']).first()
    if user is None or not user.check_password(data['password']):
        return bad_request("Invalid username or password")
    return jsonify(user.to_dict())
