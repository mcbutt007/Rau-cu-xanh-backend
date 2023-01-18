from app.api import bp
from dataclasses import dataclass
from flask import jsonify
from app.models import User
from flask import jsonify, request, url_for, abort
from app import db
from app.api.auth import token_auth
from app.api.errors import bad_request
from datetime import datetime

@bp.route("/user/<int:id>", methods=["GET"])
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())


@bp.route("/users", methods=["GET"])
def get_users():
    page = 1
    per_page = 100
    data = User.to_collection_dict(User.query, page, per_page, "api.get_users")
    return jsonify(data)


@bp.route("/users/<int:id>/followers", methods=["GET"])
def get_followers(id):
    pass


@bp.route("/users/<int:id>/followed", methods=["GET"])
def get_followed(id):
    pass


@bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json() or {}
    if "username" not in data or "email" not in data or "password" not in data:
        return bad_request("must include username, email and password fields")
    if User.query.filter_by(username=data["username"]).first():
        return bad_request("please use a different username")
    if User.query.filter_by(email=data["email"]).first():
        return bad_request("please use a different email address")
    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers["Location"] = url_for("api.get_user", id=user.id)
    return response


@bp.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json() or {}
    if (
        "username" in data
        and data["username"] != user.username
        and User.query.filter_by(username=data["username"]).first()
    ):
        return bad_request("please use a different username")
    if (
        "email" in data
        and data["email"] != user.email
        and User.query.filter_by(email=data["email"]).first()
    ):
        return bad_request("please use a different email address")
    if "birthday" in data:
        data["birthday"] = datetime.strptime(data["birthday"], '%m-%d-%Y')
    user.from_dict(data, new_user=False)
    db.session.commit()
    return jsonify(user.to_dict())

@bp.route("/changepassword", methods=["PUT"])
def changepassword():
    data = request.get_json() or {}
    if "id" not in data or "password" not in data:
        return bad_request("must include id and password fields")
    user = User.query.filter_by(id=data['id']).first()
    if user is None:
        return bad_request("Not found user")
    user.change_passwd_from_dict(data)
    db.session.commit()
    return jsonify(user.to_dict())
