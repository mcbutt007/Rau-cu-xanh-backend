from app.api import bp
from flask import jsonify
from app.models import Shop
from flask import abort
from app.api.auth import token_auth
from flask import request


@bp.route("/shop/<int:id>", methods=["GET"])
def get_shop(id):
    return jsonify(Shop.query.get_or_404(id).to_dict())


@bp.route("/shops", methods=["GET"])
def get_shops():
    page = 1
    per_page = 100
    data = Shop.to_collection_dict(Shop.query, page, per_page, "api.get_shops")
    return jsonify(data)
