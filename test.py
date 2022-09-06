from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import *

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def test_password_hashing(self):
        u = User(UserName='susan')
        u.set_password('susan1234')
        self.assertFalse(u.check_password('iloveyou1234'))
        self.assertTrue(u.check_password('susan1234'))

    def test_add_data(self):
        u1 = User(UserName='alice', Email='alice@unittest.com')
        u2 = User(UserName='bob', Email='bob@unittest.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.UserName, 'alice')
        self.assertNotEqual(u2.UserName, 'bob')

    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main(verbosity=2)
