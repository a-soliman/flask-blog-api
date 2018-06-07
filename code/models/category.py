import sqlite3
from db import db


class CategoryModel(db.Model):
    '''
    THIS CLASS CONTAINS ALL THE FUNCTION NEEDED TO CREAT, EDIT DELETE CATEGORY
    ARGS: 
        id: int
        name: string
    '''
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    posts = db.relationship('PostModel', lazy='dynamic')

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def json(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        return

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        return
