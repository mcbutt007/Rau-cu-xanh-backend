from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    profile_pic = db.Column(db.String(128))
    phone_no = db.Column(db.Integer)
    birthday = db.Column(db.DateTime)
    gender = db.Column(db.String(16))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    notifications = db.relationship('Notifications', backref='user', lazy=True)
    carts = db.relationship('Cart', backref='user', lazy=True)
    bookmarks = db.relationship('Bookmark', backref='user', lazy=True)
    reciepts = db.relationship('Reciept', backref='user', lazy=True)
    reviews = db.relationship('Review', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Reset_password_email(db.Model):
    email = db.Column(db.String(128), index=True, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow, primary_key=True)
    status = db.Column(db.String(120), index=True)

class Notifications(db.Model):
    noti_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    raucu_id = db.Column(db.Integer, db.ForeignKey('raucu.raucu_id'))
    description = db.Column(db.String(512))
    noti_type = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Reciept(db.Model):
    reciept_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    shipping_cost = db.Column(db.Numeric)
    shipping_addr = db.Column(db.Numeric)
    total_price = db.Column(db.Numeric)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Reciept_list(db.Model):
    reciept_id = db.Column(db.Integer, db.ForeignKey('reciept.reciept_id'), primary_key=True)
    raucu_id = db.Column(db.Integer, db.ForeignKey('raucu.raucu_id'), primary_key=True)
    quantity = db.Column(db.Integer)

class Cart(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    raucu_id = db.Column(db.Integer, db.ForeignKey('raucu.raucu_id'), primary_key=True)
    quantity = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Bookmark(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    raucu_id = db.Column(db.Integer, db.ForeignKey('raucu.raucu_id'), primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    

class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    stars = db.Column(db.Float)
    comments = db.Column(db.String(512))
    review_type = db.Column(db.String(64), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Shop(db.Model):
    shop_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    address = db.Column(db.String(256), index=True)
    phone_no = db.Column(db.Numeric)
    profile_pic = db.Column(db.String(128))
    no_selling = db.Column(db.Integer)
    no_sold = db.Column(db.Integer)
    review_id = db.Column(db.Integer, db.ForeignKey('review.review_id'))
    timestamp  = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Selling_list(db.Model):
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.shop_id'), primary_key=True)
    raucu_id = db.Column(db.Integer, db.ForeignKey('raucu.raucu_id'), primary_key=True)
    quantity = db.Column(db.String(120), index=True)
    status = db.Column(db.String(120), index=True)
    item_sold = db.Column(db.String(120), index=True)

class Raucu(db.Model):
    raucu_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    raucu_type = db.Column(db.String(128), index=True)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.shop_id'))
    product_pic = db.Column(db.String(128))
    price = db.Column(db.Numeric)
    description = db.Column(db.String(512))
    review_id = db.Column(db.Integer, db.ForeignKey('review.review_id'))
    discount = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
