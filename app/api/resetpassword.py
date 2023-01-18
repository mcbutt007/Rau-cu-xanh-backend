from app.api import bp
from dataclasses import dataclass
from app.models import Reset_password_email
from flask import jsonify, request, url_for, abort
from app import db
from app.api.auth import token_auth
from app.api.errors import bad_request

@bp.route("/resetpassword", methods=["POST"])
def reset_password():
    data = request.get_json() or {}
    if "email" not in data :
        return bad_request("must include email fields")
    resetpassword = Reset_password_email()
    resetpassword.from_dict(data)
    db.session.add(resetpassword)
    db.session.commit()
    response = jsonify(resetpassword.to_dict())
    response.status_code = 201
    return response
