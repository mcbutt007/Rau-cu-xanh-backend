from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import *

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def test_password_hashing(self):
        u = User(user_name='susan')
        u.set_password('susan1234')
        self.assertFalse(u.check_password('iloveyou1234'))
        self.assertTrue(u.check_password('susan1234'))

    def test_add_data(self):
        
        # User table
        u1 = User(user_name='alice', email='alice@unittest.com')
        u1.set_password('susan1234')
        u2 = User(user_name='bob', email='bob@unittest.com')
        u2.set_password('bob1234')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.user_name, 'alice')
        self.assertNotEqual(u2.user_name, 'not_bob')

        # Reset_password_email table
        email1 = Reset_password_email(email='alice@unittest.com')
        email2 = Reset_password_email(email='bob@unittest.com')
        db.session.add(email1, email2)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main(verbosity=2)
