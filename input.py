from datetime import datetime, timedelta
import unittest, os
from app import app, db
from app.models import *


class UserModelCase(unittest.TestCase):
    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
        db.create_all()

    def test_password_hashing(self):
        u = User(username='susan')
        u.set_password('susan1234')
        self.assertFalse(u.check_password('iloveyou1234'))
        self.assertTrue(u.check_password('susan1234'))

    def test_add_data(self):
        # User table
        u1 = User(username='alice', email='alice@unittest.com', phone_no='123456780',
                  birthday=datetime(2017,3,29), gender='female',
                  profile_pic='https://randomuser.me/api/portraits/women/34.jpg')
        u1.set_password('susan1234')

        u2 = User(username='bob', email='bob@unittest.com', phone_no='76453210',
                  birthday=datetime(1957,7,9), gender='male',
                  profile_pic='https://randomuser.me/api/portraits/men/34.jpg')
        u2.set_password('bob1234')

        db.session.add_all([u1, u2])

        self.assertEqual(u1.username, 'alice')
        self.assertNotEqual(u2.username, 'not_bob')

        # Reset_password_email table
        email1 = Reset_password_email(email='alice@unittest.com')
        email2 = Reset_password_email(email='bob@unittest.com')
        db.session.add_all([email1, email2])

        # Review table
        review1 = Review(user_id=1, stars=3.2, comments='average', review_type='shop')
        review2 = Review(user_id=2, stars=4.2, comments='very good', review_type='shop')
        review3 = Review(user_id=2, stars=1.0, comments='bad', review_type='raucu')
        review4 = Review(user_id=2, stars=5.0, comments='perfect', review_type='raucu')
        db.session.add_all([review1, review2, review3, review4])

        # Shop table
        shop1 = Shop(name='Bach hoa xanh', address = '234 Street street',
                     phone_no='123456780', no_selling=10, no_sold=5, review_id=1)
        shop2 = Shop(name='Rau cu xanh offical', address = '1/2/3 Duong street',
                     phone_no='1923456780', no_selling=105, no_sold=55, review_id=2)
        db.session.add_all([shop1, shop2])

        # Raucu table
        raucu1 = Raucu(name='Rau muong', raucu_type='rau xanh',shop_id=1,
                       price=5000, description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                       review_id=3, discount=0.5)
        raucu2 = Raucu(name='Ot', raucu_type='gia vi',shop_id=2,
                       price=7000, description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                       review_id=4, discount=0.5)
        db.session.add_all([raucu1, raucu2])

        # Bookmark table
        bookmark1 = Bookmark(user_id=1,raucu_id=1)
        bookmark2 = Bookmark(user_id=1,raucu_id=2)
        bookmark3 = Bookmark(user_id=2,raucu_id=1)
        bookmark4 = Bookmark(user_id=2,raucu_id=2)
        db.session.add_all([bookmark1, bookmark2, bookmark3, bookmark4])

        # Cart table
        cart1 = Cart(user_id=1,raucu_id=1,quantity=40)
        cart2 = Cart(user_id=1,raucu_id=2,quantity=13)
        cart3 = Cart(user_id=2,raucu_id=1,quantity=12)
        cart4 = Cart(user_id=2,raucu_id=2,quantity=11)
        db.session.add_all([cart1, cart2, cart3, cart4])

        # Notifications table
        noti1 = Notifications(user_id=1,raucu_id=1,description='Sale off 20%',noti_type='sale_off')
        noti2 = Notifications(user_id=1,raucu_id=2,description='Sale off 30%',noti_type='sale_off')
        noti3 = Notifications(user_id=2,raucu_id=1,description='Sale off 25%',noti_type='sale_off')
        noti4 = Notifications(user_id=2,raucu_id=2,description='Sale off 10%',noti_type='sale_off')
        db.session.add_all([noti1, noti2, noti3, noti4])

        # Selling_list table
        selling1 = Selling_list(shop_id=1,raucu_id=1,quantity=222,status='selling',item_sold=32)
        selling2 = Selling_list(shop_id=2,raucu_id=2,quantity=0,status='out_of_stock',item_sold=332)
        db.session.add_all([selling1, selling2])

        # commit
        db.session.commit()
if __name__ == '__main__':
    app.config['TESTING'] = True
    unittest.main(verbosity=2)
