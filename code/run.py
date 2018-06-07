from app import app
from db import db

db.init_app(app)

# SQLAlchemy to create all the necesiry tables before start (IMPORTANT FOR HEROKU)
@app.before_first_request
def create_tables():
    print('Creating tables')
    db.create_all()