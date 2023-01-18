from app.api import bp
from flask import jsonify, abort, request
from app.models import Raucu
from app.api.auth import token_auth


@bp.route("/raucu/<int:id>", methods=["GET"])
def get_raucu(id):
    return jsonify(Raucu.query.get_or_404(id).to_dict())


@bp.route("/rauculist", methods=["GET"])
def get_raucu_list():
    page = 1
    per_page = 100
    try:
        data = request.get_json() or {}
        if "raucu_type" in data:
            raucu = Raucu.to_collection_dict(Raucu.query.filter_by(raucu_type=data['raucu_type']), page, per_page, "api.get_raucu_list")
            return jsonify(raucu)
        elif "shop_id" in data:
            raucu = Raucu.to_collection_dict(Raucu.query.filter_by(shop_id=data['shop_id']), page, per_page, "api.get_raucu_list")
            return jsonify(raucu)
    except:
        response = Raucu.to_collection_dict(
            Raucu.query, page, per_page, "api.get_raucu_list"
        )
    return jsonify(response)
