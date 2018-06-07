from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required, current_identity

from werkzeug.security import generate_password_hash, check_password_hash


from models.user import UserModel


class User(Resource):
    def get(self, email):
        user = UserModel.find_by_email(email)

        if user is None:
            return {'success': False, 'message': 'User not found'}, 404
        return user.json(), 400

    def delete(self, email):
        user = UserModel.find_by_email(email)

        if user is None:
            return {'success': False, 'message': 'User not found.'}, 404

        # try deleting the user
        try:
            user.delete_from_db()
        except:
            return {'success': False, 'message': 'Something went wrong.'}, 500
        return {'success': True, 'message': 'User removed successfully.'}, 200


class UserInformation(Resource):
    @jwt_required()
    def get(self, id):
        print('identent ', current_identity.id)
        print('id: ', id)
        if str(current_identity.id) != id:
            return {'success': False, 'message': 'Not Authorized'}, 401

        user = UserModel.find_by_id(id)

        if user is None:
            return {'success': False, 'message': 'User not found'}, 404
        return user.json(), 200


class ListUsers(Resource):
    def get(self):
        return {'users': [user.json() for user in UserModel.query.all()]}


class RegisterUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='username is required.')
    parser.add_argument('password', type=str, required=True, help='password is required.')
    parser.add_argument('email', type=str, required=True, help='email is required.')

    def post(self):
        data = RegisterUser.parser.parse_args()

        # check if the user's email already exists in the DB
        if UserModel.find_by_email(data['email']):
            return {'success': False, 'message': 'a user with the provided email already exists'}

        # Hash the password
        pw_hash = generate_password_hash(data['password'])
        user = UserModel(None, data['username'], pw_hash, data['email'])

        # try to save the user to DB
        try:
            user.save_to_db()
        except:
            return {'success': False, 'message': 'Something went wrong'}, 500

        return {'success': True, 'message': 'user created successfully'}, 201
