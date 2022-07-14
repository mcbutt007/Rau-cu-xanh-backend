from datetime import datetime
from app import db

class User(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(64), index=True, unique=True)
    Email = db.Column(db.String(120), index=True, unique=True)
    PasswordHash = db.Column(db.String(128))
    ProfilePic = db.Column(db.String(128))
    PhoneNo = db.Column(db.Numeric)
    Birthday = db.Column(db.DateTime)
    Gender = db.Column(db.String(128))
    TimeRegistered  = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Reset_Password_Email(db.Model):
    Email = db.Column(db.String(64), index=True, unique=True)
    TimeStamp = db.Column(db.String(120), index=True, unique=True)

class Notifications(db.Model):
    NotiID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.String(64), index=True, unique=True)
    RaucuID = db.Column(db.String(120), index=True, unique=True)
    TypeID = db.Column(db.String(128))
    Description = db.Column(db.String(128))
    TimeStamp = db.Column(db.Numeric)

class Noti_Type(db.Model):
    NotiTypeID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64), index=True, unique=True)
    Description = db.Column(db.String(120), index=True, unique=True)

class Reciept(db.Model):
    RecieptID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.String(64), index=True, unique=True)
    ShippingCost = db.Column(db.String(120), index=True, unique=True)
    ShippingAddr = db.Column(db.String(128))
    TotalPrice = db.Column(db.String(128))
    CreatedTime = db.Column(db.Numeric)

class Reciept_List(db.Model):
    RecieptID = db.Column(db.Integer, primary_key=True)
    RaucuID = db.Column(db.String(64), index=True, unique=True)
    Quantity = db.Column(db.String(120), index=True, unique=True)

class Cart(db.Model):
    CartID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.String(64), index=True, unique=True)
    RaucuID = db.Column(db.String(120), index=True, unique=True)
    Quantity = db.Column(db.String(120), index=True, unique=True)
    TimeStamp = db.Column(db.String(120), index=True, unique=True)

class Bookmark(db.Model):
    BookmarkID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.String(64), index=True, unique=True)
    RaucuID = db.Column(db.String(120), index=True, unique=True)
    TimeStamp = db.Column(db.String(120), index=True, unique=True)

class Review(db.Model):
    ReviewID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.String(64), index=True, unique=True)
    Stars = db.Column(db.String(120), index=True, unique=True)
    Comments = db.Column(db.String(120), index=True, unique=True)
    ReviewType = db.Column(db.String(120), index=True, unique=True)
    TimeStamp = db.Column(db.String(120), index=True, unique=True)

class ReviewType(db.Model):
    TypeID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64), index=True, unique=True)
    RaucuID = db.Column(db.String(120), index=True, unique=True)
    ShopID = db.Column(db.String(120), index=True, unique=True)
    TimeStamp = db.Column(db.String(120), index=True, unique=True)

class Shop(db.Model):
    ShopID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64), index=True, unique=True)
    Address = db.Column(db.String(120), index=True, unique=True)
    PhoneNo = db.Column(db.String(120), index=True, unique=True)
    ProfilePic = db.Column(db.String(120), index=True, unique=True)
    TimeCreated = db.Column(db.String(120), index=True, unique=True)
    NoSelling = db.Column(db.String(120), index=True, unique=True)
    NoSold = db.Column(db.String(120), index=True, unique=True)
    ReviewID = db.Column(db.String(120), index=True, unique=True)

class Selling_List(db.Model):
    ShopID = db.Column(db.Integer, primary_key=True)
    RaucuID = db.Column(db.String(64), index=True, unique=True)
    Quantity = db.Column(db.String(120), index=True, unique=True)
    Status = db.Column(db.String(120), index=True, unique=True)
    ItemSold = db.Column(db.String(120), index=True, unique=True)

class Raucu(db.Model):
    RaucuID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64), index=True, unique=True)
    Type = db.Column(db.String(120), index=True, unique=True)
    ShopID = db.Column(db.String(120), index=True, unique=True)
    ProductPic = db.Column(db.String(120), index=True, unique=True)
    Price = db.Column(db.String(120), index=True, unique=True)
    Description = db.Column(db.String(120), index=True, unique=True)
    ReviewID = db.Column(db.String(120), index=True, unique=True)
    TimeCreated = db.Column(db.String(120), index=True, unique=True)
    Discount = db.Column(db.String(120), index=True, unique=True)
