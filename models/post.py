import sqlite3
from db import db


class PostModel(db.Model):
    '''
    THIS CLASS CONTAINS ALL THE FUNCTION NEEDED TO
    CREAT, EDIT DELETE AND ADD POST

    Args: 
        _id: int
        title: string
        body: string
        user: int => reference to the user's_id
        category_id: int => reference to the category's id (Foreign key)
        owner: DO NOT SET THIS VALUE WHILE INSERTING, IT WILL CHANGE AFTER CHECKING THE ACCESS TOKEN.
    '''

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.String(2000))
    user = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('CategoryModel')

    def __init__(self, _id, title, body, user, category_id, owner=None):
        self.id = _id
        self.title = title
        self.body = body
        self.user = user
        self.category_id = category_id
        self.owner = None

    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "user": self.user,
            "category_id": self.category_id,
            "owner": self.owner
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_userid(cls, user_id):
        return cls.query.filter_by(user=user_id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        return

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        return
