from datetime import datetime
from dataclasses import dataclass
from app import login, db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import base64
from datetime import datetime, timedelta
import os


class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        resources = query.paginate(page=page, per_page=per_page, error_out=False)
        data = [item.to_dict() for item in resources.items]
        return data


class User(UserMixin, PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    profile_pic = db.Column(db.String, default="https://t3.ftcdn.net/jpg/05/00/54/28/360_F_500542898_LpYSy4RGAi95aDim3TLtSgCNUxNlOlcM.jpg")
    phone_no = db.Column(db.String)
    birthday = db.Column(db.DateTime)
    gender = db.Column(db.String(16))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)
    notifications = db.relationship("Notifications", backref="user", lazy=True)
    carts = db.relationship("Cart", backref="user", lazy=True)
    bookmarks = db.relationship("Bookmark", backref="user", lazy=True)
    receipts = db.relationship("Receipt", backref="user", lazy=True)
    reviews = db.relationship("Review", backref="user", lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User {}>".format(self.username)

    def to_dict(self):
        data = {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "profile_pic": self.profile_pic,
            "phone_no": self.phone_no,
            "birthday": self.birthday,
            "gender": self.gender,
            "timestamp": self.timestamp.strftime("%Y-%m-%d"),
        }
        return data

    def from_dict(self, data, new_user=False):
        for field in [
            "username",
            "email",
            "profile_pic",
            "phone_no",
            "birthday",
            "gender",
        ]:
            if field in data:
                setattr(self, field, data[field])
        if new_user and "password" in data:
            self.set_password(data["password"])

    def change_passwd_from_dict(self, data):
        self.set_password(data["password"])

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode("utf-8")
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user


class Reset_password_email(db.Model):
    email = db.Column(db.String(128), index=True, primary_key=True)
    status = db.Column(db.String(120), index=True, default="NotChecked")
    timestamp = db.Column(
        db.DateTime, index=True, default=datetime.utcnow, primary_key=True
    )
    def to_dict(self):
        data = {
            "email": self.email,
            "status": self.status,
            "timestamp": self.timestamp.strftime("%Y-%m-%d"),
        }
        return data

    def from_dict(self, data):
        for field in [
            "email",
        ]:
            if field in data:
                setattr(self, field, data[field])


class Notifications(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    icon = db.Column(db.String)
    raucu_id = db.Column(db.Integer, db.ForeignKey("raucu.id"))
    receipt_id = db.Column(db.Integer, db.ForeignKey("receipt.id"))
    description = db.Column(db.String(512))
    noti_type = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        data = {
            "id": self.id,
            "icon": self.icon,
            "user_id": self.user_id,
            "receipt_id": self.receipt_id,
            "raucu_id": self.raucu_id,
            "description": self.description,
            "noti_type": self.noti_type,
            "timestamp": self.timestamp.strftime("%Y-%m-%d"),
        }
        return data

    def from_dict(self, data):
        for field in [
            "user_id",
            "icon",
            "receipt_id",
            "raucu_id",
            "description",
            "noti_type",
        ]:
            if field in data:
                setattr(self, field, data[field])

class Receipt(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    shipping_cost = db.Column(db.Integer)
    shipping_addr = db.Column(db.String)
    total_price = db.Column(db.Integer)
    order_status = db.Column(db.String, default="chuathanhtoan")
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def from_dict(self, data):
        for field in [
            "user_id",
            "shipping_cost",
            "shipping_addr",
            "order_status",
            "total_price",
        ]:
            if field in data:
                setattr(self, field, data[field])

    def to_dict(self):
        data = {
            "id": self.id,
            "user_id": self.user_id,
            "shipping_cost": self.shipping_cost,
            "shipping_addr": self.shipping_addr,
            "total_price": self.total_price,
            "order_status": self.order_status,
            "timestamp": self.timestamp.strftime("%Y-%m-%d"),
        }
        return data

class Receipt_list(PaginatedAPIMixin, db.Model):
    receipt_id = db.Column(db.Integer, db.ForeignKey("receipt.id"), primary_key=True)
    raucu_id = db.Column(db.Integer, db.ForeignKey("raucu.id"), primary_key=True)
    quantity = db.Column(db.Integer)

    def to_dict(self):
        data = {
            "receipt_id": self.receipt_id,
            "raucu_id": self.raucu_id,
            "quantity": self.quantity,
        }
        return data

    def from_dict(self, data):
        for field in [
            "receipt_id",
            "raucu_id",
            "quantity",
        ]:
            if field in data:
                setattr(self, field, data[field])

class Cart(PaginatedAPIMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    raucu_id = db.Column(db.Integer, db.ForeignKey("raucu.id"), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        data = {
            "user_id": self.user_id,
            "raucu_id": self.raucu_id,
            "quantity": self.quantity,
            "timestamp": self.timestamp.strftime("%Y-%m-%d"),
        }
        return data

    def from_dict(self, data):
        for field in [
            "user_id",
            "raucu_id",
            "quantity",
        ]:
            if field in data:
                setattr(self, field, data[field])

class Bookmark(PaginatedAPIMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    raucu_id = db.Column(db.Integer, db.ForeignKey("raucu.id"), primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        data = {
            "user_id": self.user_id,
            "raucu_id": self.raucu_id,
            "timestamp": self.timestamp.strftime("%Y-%m-%d"),
        }
        return data

    def from_dict(self, data):
        for field in [
            "user_id",
            "raucu_id",
        ]:
            if field in data:
                setattr(self, field, data[field])

class Review(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer, db.ForeignKey("shop.id"))
    raucu_id = db.Column(db.Integer, db.ForeignKey("raucu.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    stars = db.Column(db.Float)
    comments = db.Column(db.String(512))
    review_type = db.Column(db.String(64), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        data = {
            "id": self.id,
            "raucu_id": self.raucu_id,
            "shop_id": self.shop_id,
            "user_id": self.user_id,
            "stars": self.stars,
            "comments": self.comments,
            "review_type": self.review_type,
            "timestamp": self.timestamp.strftime("%Y-%m-%d"),
        }
        return data

    def from_dict(self, data):
        for field in [
            "raucu_id",
            "shop_id",
            "user_id",
            "stars",
            "comments",
            "review_type",
        ]:
            if field in data:
                setattr(self, field, data[field])

class Shop(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    address = db.Column(db.String(256), index=True)
    phone_no = db.Column(db.String)
    profile_pic = db.Column(db.String)
    no_selling = db.Column(db.Integer, default=0)
    no_sold = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    reviews = db.relationship("Review", backref="shop", lazy=True)
    selling_list = db.relationship("Selling_list", backref="shop", lazy=True)

    def to_dict(self):
        data = {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone_no": self.phone_no,
            "profile_pic": self.profile_pic,
            "no_selling": self.no_selling,
            "no_sold": self.no_sold,
            "timestamp": self.timestamp.strftime("%Y-%m-%d"),
        }
        return data

    def from_dict(self, data):
        for field in [
            "id",
            "name",
            "address",
            "phone_no",
            "profile_pic",
            "no_selling",
            "no_sold",
        ]:
            if field in data:
                setattr(self, field, data[field])

class Selling_list(PaginatedAPIMixin, db.Model):
    shop_id = db.Column(db.Integer, db.ForeignKey("shop.id"), primary_key=True)
    raucu_id = db.Column(db.Integer, db.ForeignKey("raucu.id"), primary_key=True)
    quantity = db.Column(db.String(120), index=True)
    status = db.Column(db.String(120), index=True)
    item_sold = db.Column(db.String(120), index=True)

    def to_dict(self):
        data = {
            "shop_id": self.shop_id,
            "raucu_id": self.raucu_id,
            "quantity": self.quantity,
            "status": self.status,
            "item_sold": self.item_sold,
        }
        return data
    def from_dict(self, data):
        for field in [
            "shop_id",
            "raucu_id",
            "quantity",
            "status",
            "item_sold",
        ]:
            if field in data:
                setattr(self, field, data[field])


class Raucu(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    raucu_type = db.Column(db.String(128), index=True, nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey("shop.id"))
    product_pic = db.Column(db.String)
    price = db.Column(db.Integer)
    description = db.Column(db.String(512))
    discount = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        data = {
            "id": self.id,
            "name": self.name,
            "raucu_type": self.raucu_type,
            "shop_id": self.shop_id,
            "product_pic": self.product_pic,
            "price": self.price,
            "description": self.description,
            "discount": self.discount,
            "timestamp": self.timestamp.strftime("%Y-%m-%d"),
        }
        return data

    def from_dict(self, data):
        for field in [
            "id",
            "name",
            "raucu_type",
            "shop_id",
            "product_pic",
            "price",
            "description",
            "discount",
        ]:
            if field in data:
                setattr(self, field, data[field])
