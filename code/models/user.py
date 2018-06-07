import sqlite3
from db import db


class UserModel(db.Model):
    '''
    THIS CLASS CONTAINS ALL THE FUNCTION NEEDED TO
    CREAT, EDIT DELETE AND ADD USER

    Args:
    _id: int
    username: string
    password: string,
    email: string
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    email = db.Column(db.String(80))

    def __init__(self, _id, username, password, email):
        self.id = _id
        self.username = username
        self.password = password
        self.email = email

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'email': self.email
        }

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        return

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        return
