from app.api import bp
from dataclasses import dataclass
from app.models import Receipt, Receipt_list, Notifications
from flask import jsonify, request, url_for, abort
from app import db
from app.api.auth import token_auth
from app.api.errors import bad_request


@bp.route("/receipt/<int:id>", methods=["GET"])
def get_receipt(id):
    return jsonify(Receipt.query.get_or_404(id).to_dict())


@bp.route("/receipts", methods=["GET"])
def get_receipts():
    page = 1
    per_page = 100
    try:
        data = request.get_json() or {}
        if "user_id" in data:
            usrReceipt = Receipt.to_collection_dict(Receipt.query.filter_by(user_id=data['user_id']), page, per_page, "api.get_receipt")
            return jsonify(usrReceipt)
    except:
        response = Receipt.to_collection_dict(
            Receipt.query, page, per_page, "api.get_receipt"
        )
    return jsonify(response)

@bp.route("/receiptlist", methods=["GET"])
def get_receiptlist():
    page = 1
    per_page = 100
    data = Receipt_list.to_collection_dict(
        Receipt_list.query, page, per_page, "api.get_receipt"
    )
    return jsonify(data)

@bp.route("/receiptlist", methods=["POST"])
def create_receiptlist():
    data = request.get_json() or {}
    item = ["receipt_id","raucu_id","quantity"]
    for element in item:
        if element not in data:
            return bad_request("Missing " + element)
    receiptlist = Receipt_list()
    receiptlist.from_dict(data)
    db.session.add(receiptlist)
    db.session.commit()
    response = jsonify(receiptlist.to_dict())
    response.status_code = 201
    return response

@bp.route("/receipts", methods=["POST"])
def create_receipt():
    data = request.get_json() or {}
    item = ["user_id","shipping_cost","shipping_addr", "total_price"]
    for element in item:
        if element not in data:
            return bad_request("Missing " + element)
    receipt = Receipt()
    receipt.from_dict(data)
    db.session.add(receipt)
    db.session.commit()

    noti = Notifications()
    noti.user_id = receipt.user_id
    noti.noti_type = "dangiao"
    noti.receipt_id = receipt.id
    noti.description = "Đơn hàng #{} đang được giao.".format(receipt.id)
    noti.icon= "https://static.vecteezy.com/system/resources/thumbnails/002/206/240/small/fast-delivery-icon-free-vector.jpg"
    db.session.add(noti)

    db.session.commit()
    response = jsonify(receipt.to_dict())
    response.status_code = 201
    response.headers["Location"] = url_for("api.get_receipt", id=receipt.id)
    return response

@bp.route("/receipts", methods=["PUT"])
def change_receipt_state():
    data = request.get_json() or {}
    if "id" not in data :
        return bad_request("must include id fields")
    receipt = Receipt.query.filter_by(id=data['id']).first()
    if receipt is None:
        return bad_request("Not found receipt")
    receipt.from_dict(data)
    db.session.commit()

    if (data["order_status"]=="dahuy"):
        noti = Notifications()
        noti.user_id = receipt.user_id
        noti.noti_type = "huydon"
        noti.receipt_id = receipt.id
        noti.description = "Đơn hàng #{} đã được hủy.".format(receipt.id)
        noti.icon = "https://static.thenounproject.com/png/1318245-200.png"
        db.session.add(noti)
        db.session.commit()

    return jsonify(receipt.to_dict())
