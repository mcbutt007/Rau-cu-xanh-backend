from app.api import bp
from flask import jsonify
from app.models import Notifications
from flask import abort
from app.api.auth import token_auth
from flask import request


@bp.route("/notification/<int:id>", methods=["GET"])
def get_notification(id):
    return jsonify(Notifications.query.get_or_404(id).to_dict())


@bp.route("/notifications", methods=["GET"])
def get_notifications():
    page = 1
    per_page = 100
    data = Notifications.to_collection_dict(
        Notifications.query, page, per_page, "api.get_notifications"
    )
    return jsonify(data)
