from app.api import bp
from dataclasses import dataclass
from flask import jsonify
from app.models import Bookmark
from flask import jsonify, request, url_for, abort
from app import db
from app.api.auth import token_auth
from app.api.errors import bad_request

@bp.route("/bookmarks", methods=["GET"])
def get_bookmarks():
    page = 1
    per_page = 100
    data = Bookmark.to_collection_dict(Bookmark.query, page, per_page, "api.get_bookmarks")
    return jsonify(data)

@bp.route("/bookmarks", methods=["POST"])
def create_bookmarks():
    data = request.get_json() or {}
    if "user_id" not in data or "raucu_id" not in data:
        return bad_request("must include user_id and raucu_id fields")
    bookmark = Bookmark()
    bookmark.from_dict(data)
    db.session.add(bookmark)
    db.session.commit()
    response = jsonify(bookmark.to_dict())
    response.status_code = 201
    response.headers["Location"] = url_for("api.get_bookmarks")
    return response

@bp.route('/bookmarks', methods=['DELETE'])
def delete_bookmark():
    data = request.get_json() or {}
    if "user_id" not in data or "raucu_id" not in data:
        return bad_request("must include user_id and raucu_id fields")
    bookmark = Bookmark.query.filter_by(user_id=data['user_id'], raucu_id=data['raucu_id']).first()
    db.session.delete(bookmark)
    db.session.commit()
    return 'Delete success', 200
