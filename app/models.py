from datetime import datetime
from app import login, db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    profile_pic = db.Column(db.String(128))
    phone_no = db.Column(db.String)
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
    def __repr__(self):
        return '<User {}>'.format(self.username)
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Reset_password_email(db.Model):
    email = db.Column(db.String(128), index=True, primary_key=True)
    status = db.Column(db.String(120), index=True, default='NotChecked')
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow, primary_key=True)

class Notifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    raucu_id = db.Column(db.Integer, db.ForeignKey('raucu.id'))
    description = db.Column(db.String(512))
    noti_type = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Reciept(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    shipping_cost = db.Column(db.Numeric)
    shipping_addr = db.Column(db.Numeric)
    total_price = db.Column(db.Numeric)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Reciept_list(db.Model):
    reciept_id = db.Column(db.Integer, db.ForeignKey('reciept.id'), primary_key=True)
    raucu_id = db.Column(db.Integer, db.ForeignKey('raucu.id'), primary_key=True)
    quantity = db.Column(db.Integer)

class Cart(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    raucu_id = db.Column(db.Integer, db.ForeignKey('raucu.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Bookmark(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    raucu_id = db.Column(db.Integer, db.ForeignKey('raucu.id'), primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    stars = db.Column(db.Float)
    comments = db.Column(db.String(512))
    review_type = db.Column(db.String(64), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    address = db.Column(db.String(256), index=True)
    phone_no = db.Column(db.String)
    profile_pic = db.Column(db.String(128))
    no_selling = db.Column(db.Integer, default=0)
    no_sold = db.Column(db.Integer, default=0)
    review_id = db.Column(db.Integer, db.ForeignKey('review.id'))
    timestamp  = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    reviews = db.relationship('Review', backref='shop', lazy=True)
    selling_list = db.relationship('Selling_list', backref='shop', lazy=True)

class Selling_list(db.Model):
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), primary_key=True)
    raucu_id = db.Column(db.Integer, db.ForeignKey('raucu.id'), primary_key=True)
    quantity = db.Column(db.String(120), index=True)
    status = db.Column(db.String(120), index=True)
    item_sold = db.Column(db.String(120), index=True)

class Raucu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    raucu_type = db.Column(db.String(128), index=True, nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'))
    product_pic = db.Column(db.String(128))
    price = db.Column(db.Integer)
    description = db.Column(db.String(512))
    review_id = db.Column(db.Integer, db.ForeignKey('review.id'))
    discount = db.Column(db.Float)
    timestamp  = db.Column(db.DateTime, index=True, default=datetime.utcnow)
