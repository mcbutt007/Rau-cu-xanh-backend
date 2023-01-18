from flask import Blueprint

bp = Blueprint("api", __name__)

from app.api import (
    login,
    users,
    resetpassword,
    errors,
    tokens,
    raucu,
    notifications,
    receipts,
    carts,
    bookmarks,
    reviews,
    shops,
)
