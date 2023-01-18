from app.api import bp
from dataclasses import dataclass
from flask import jsonify
from app.models import Cart
from flask import jsonify, request, url_for, abort
from app import db
from app.api.auth import token_auth
from app.api.errors import bad_request
from flask import request


@bp.route("/carts", methods=["GET"])
def get_carts():
    page = 1
    per_page = 100
    data = Cart.to_collection_dict(Cart.query, page, per_page, "api.carts")
    return jsonify(data)

@bp.route("/carts", methods=["POST"])
def create_cart():
    data = request.get_json() or {}
    if "user_id" not in data or "raucu_id" not in data or "quantity" not in data:
        return bad_request("must include user_id, raucu_id and quantity fields")
    cart = Cart.query.filter_by(user_id=data['user_id'], raucu_id=data['raucu_id']).first()
    if cart is None:
        cart = Cart()
        cart.from_dict(data)
        db.session.add(cart)
        db.session.commit()
    else:
        cart.quantity = cart.quantity + int(data["quantity"])
        db.session.commit()
    response = jsonify(cart.to_dict())
    response.status_code = 201
    response.headers["Location"] = url_for("api.get_carts")
    return response

@bp.route("/carts", methods=["PUT"])
def update_cart():
    data = request.get_json() or {}
    if "user_id" not in data or "raucu_id" not in data or "quantity" not in data:
        return bad_request("must include user_id, raucu_id and quantity fields")
    cart = Cart.query.filter_by(user_id=data['user_id'], raucu_id=data['raucu_id']).first()
    if cart is None:
        return bad_request("Not found cart")
    cart.from_dict(data)
    db.session.commit()
    return jsonify(cart.to_dict())

@bp.route("/carts", methods=["DELETE"])
def delete_cart():
    data = request.get_json() or {}
    if "user_id" not in data or "raucu_id" not in data:
        return bad_request("must include user_id and raucu_id fields")
    cart = Cart.query.filter_by(user_id=data['user_id'], raucu_id=data['raucu_id']).first()
    db.session.delete(cart)
    db.session.commit()
    return 'Delete success', 200
