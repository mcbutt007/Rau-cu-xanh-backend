from app.api import bp
from dataclasses import dataclass
from flask import jsonify
from app.models import Review
from flask import jsonify, request, url_for, abort
from app import db
from app.api.auth import token_auth
from app.api.errors import bad_request


@bp.route("/review/<int:id>", methods=["GET"])
def get_review(id):
    return jsonify(Review.query.get_or_404(id).to_dict())

@bp.route("/reviews", methods=["GET"])
def get_reviews():
    page = 1
    per_page = 100
    try:
        data = request.get_json() or {}
        if "raucu_id" in data:
            review = Review.to_collection_dict(Review.query.filter_by(raucu_id=data['raucu_id']), page, per_page, "api.get_reviews")
            return jsonify(review)
        elif "shop_id" in data:
            review = Review.to_collection_dict(Review.query.filter_by(shop_id=data['shop_id']), page, per_page, "api.get_reviews")
            return jsonify(review)
    except:
        data = Review.to_collection_dict(Review.query, page, per_page, "api.get_reviews")
    return jsonify(data)

@bp.route("/reviews", methods=["PUT"])
def edit_review():
    data = request.get_json() or {}
    if "user_id" not in data:
        return bad_request("must include user_id fields")
    elif "raucu_id" in data:
        review = Review.query.filter_by(user_id=data['user_id'], raucu_id=data['raucu_id']).first()
    elif "shop_id" in data:
        review = Review.query.filter_by(user_id=data['user_id'], shop_id=data['shop_id']).first()
    
    if review is None:
        return bad_request("Not found review")
    data = request.get_json() or {}
    review.from_dict(data)
    db.session.commit()
    return jsonify(review.to_dict())

@bp.route("/reviews", methods=["POST"])
def create_review():
    data = request.get_json() or {}
    if "user_id" not in data:
        return bad_request("must include user_id fields")
    review = Review()
    review.from_dict(data)
    db.session.add(review)
    db.session.commit()
    response = jsonify(review.to_dict())
    response.status_code = 201
    return response
