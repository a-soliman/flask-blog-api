from flask import Flask, request, jsonify
from flask_restful import Api, reqparse
from flask_jwt import JWT, jwt_required
import datetime

from security import authenticate, identity

# resources
from resources.login import Login  # google oauth
from resources.user import User, UserInformation, RegisterUser, ListUsers
from resources.post import Post, AddPost, ListPosts
from resources.category import Category, CategoryList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# Allows Origin for the front end to interact.
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

api = Api(app)

app.secret_key = 'super_secret_key'
# config JWT to expire within half an hour
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=365)
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
jwt = JWT(app, authenticate, identity)  # created /auth


@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
    return jsonify({
        'access_token': access_token.decode('utf-8'),
        'user_id': identity.id
    })

# configration for SQLALCHEMT
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api.add_resource(Login, '/login')
api.add_resource(ListUsers, '/users')
api.add_resource(User, '/user/<string:email>')
api.add_resource(UserInformation, '/user_id/<string:id>')
api.add_resource(RegisterUser, '/user/register')

api.add_resource(ListPosts, '/posts')
api.add_resource(Post, '/post/<string:id>')
api.add_resource(AddPost, '/post/add')

api.add_resource(CategoryList, '/categories')
api.add_resource(Category, '/category/<string:name>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5555, debug=True)
