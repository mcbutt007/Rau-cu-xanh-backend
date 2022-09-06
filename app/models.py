from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(64), index=True, unique=True)
    Email = db.Column(db.String(128), index=True, unique=True)
    PasswordHash = db.Column(db.String(128))
    ProfilePic = db.Column(db.String(128))
    PhoneNo = db.Column(db.Numeric)
    Birthday = db.Column(db.DateTime)
    Gender = db.Column(db.String(16))
    TimeRegistered = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def set_password(self, password):
        self.PasswordHash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.PasswordHash, password)

class Reset_password_email(db.Model):
    ResetID = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.String(128), index=True)
    TimeStamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Noti_type(db.Model):
    NotiTypeID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64), index=True)
    Description = db.Column(db.String(512))

class Notifications(db.Model):
    NotiID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('user.UserID'))
    RaucuID = db.Column(db.Integer, db.ForeignKey('raucu.RaucuID'))
    TypeID = db.Column(db.Integer, db.ForeignKey('noti_type.NotiTypeID'))
    Description = db.Column(db.String(512))
    TimeStamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Reciept(db.Model):
    RecieptID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('user.UserID'))
    ShippingCost = db.Column(db.Numeric)
    ShippingAddr = db.Column(db.Numeric)
    TotalPrice = db.Column(db.Numeric)
    CreatedTime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Reciept_list(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    RecieptID = db.Column(db.Integer, db.ForeignKey('reciept.RecieptID'))
    RaucuID = db.Column(db.Integer, db.ForeignKey('raucu.RaucuID'))
    Quantity = db.Column(db.Integer)

class Cart(db.Model):
    CartID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('user.UserID'))
    RaucuID = db.Column(db.Integer, db.ForeignKey('raucu.RaucuID'))
    Quantity = db.Column(db.Integer)
    TimeStamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Bookmark(db.Model):
    BookmarkID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('user.UserID'))
    RaucuID = db.Column(db.Integer, db.ForeignKey('raucu.RaucuID'))
    TimeStamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Review(db.Model):
    ReviewID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('user.UserID'))
    Stars = db.Column(db.Float)
    Comments = db.Column(db.String(512))
    ReviewType = db.Column(db.Integer, db.ForeignKey('review_type.TypeID'))
    TimeStamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Review_type(db.Model):
    TypeID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64), index=True)
    RaucuID = db.Column(db.Integer, db.ForeignKey('raucu.RaucuID'))
    ShopID = db.Column(db.Integer, db.ForeignKey('shop.ShopID'))

class Shop(db.Model):
    ShopID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64), index=True, unique=True)
    Address = db.Column(db.String(256), index=True)
    PhoneNo = db.Column(db.Numeric)
    ProfilePic = db.Column(db.String(128))
    NoSelling = db.Column(db.Integer)
    NoSold = db.Column(db.Integer)
    ReviewID = db.Column(db.Integer, db.ForeignKey('review.ReviewID'))
    TimeCreated  = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Selling_list(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    ShopID = db.Column(db.Integer, db.ForeignKey('shop.ShopID'))
    RaucuID = db.Column(db.Integer, db.ForeignKey('raucu.RaucuID'))
    Quantity = db.Column(db.String(120), index=True, unique=True)
    Status = db.Column(db.String(120), index=True, unique=True)
    ItemSold = db.Column(db.String(120), index=True, unique=True)

class Raucu(db.Model):
    RaucuID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64), index=True, unique=True)
    Type = db.Column(db.String(128), index=True)
    ShopID = db.Column(db.Integer, db.ForeignKey('shop.ShopID'))
    ProductPic = db.Column(db.String(128))
    Price = db.Column(db.Numeric)
    Description = db.Column(db.String(512))
    ReviewID = db.Column(db.Integer, db.ForeignKey('review.ReviewID'))
    Discount = db.Column(db.Float)
    TimeCreated = db.Column(db.DateTime, index=True, default=datetime.utcnow)
