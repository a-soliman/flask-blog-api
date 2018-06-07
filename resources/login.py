from flask import request, jsonify
from flask import session as login_session
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash

from flask_jwt import JWT, jwt_required

from oauth2client.client import flow_from_clientsecrets, FlowExchangeError
import httplib2
import json
import requests
import random
import string

from models.user import UserModel
import security
import os

# refrencing the client secret file
CLIENT_ID = json.loads(
    open('/var/www/html/items-rest/client_secrets.json', 'r').read())['web']['client_id']


class Login(Resource):
    def post(self):
        data = request.data
        args = json.loads(data.decode('utf-8'))

        # check if data were passed
        if args['code'] is None:
            return {
                'success': False,
                'Message': 'Invalid request.'
                }, 400

        # Collect the login data
        code = args['code']

        try:
            # upgrade the authorization code into a credentials object
            oauth_flow = flow_from_clientsecrets('/var/www/html/items-rest/client_secrets.json', scope='')
            oauth_flow.redirect_uri = 'postmessage'
            credentials = oauth_flow.step2_exchange(code)
            access_token = credentials.access_token

        except FlowExchangeError:
            return {
                'Success': False,
                'Message': 'Faild to upgrade the authorization code.'
                }, 401

        # Check that the access token is valid
        url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={}'.format(access_token))
        h = httplib2.Http()
        result = json.loads(h.request(url, 'GET')[1].decode('utf-8'))

        # if there was an error in the access token info, abort
        if result.get('error') is not None:
            return {
                'Sucess': False,
                'Message': result.get('error')
                }, 500

        # Verify that the access token is used for the intended user
        gplus_id = credentials.id_token['sub']
        if result['user_id'] != gplus_id:
            return {
                'Success': False,
                'Message': "Token's user ID dosn't match given user ID."
                }, 401

        # Verify that the access token is valid for this app
        if result['issued_to'] != CLIENT_ID:
            return {
                'Success': False,
                'Message': "Token's client ID does not match app's"
                }, 401

        # Store the access Token in the session for later use
        Login.stored_access_token = access_token

        # Get user info
        userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
        params = {'access_token': access_token}
        answer = requests.get(userinfo_url, params=params)
        data = json.loads(answer.text)

        # store user info
        if len(data['name']) < 1:
            name = data['email']
        else:
            name = data['name']
        password = generate_password_hash('default_password')
        email = data['email']
        picture = data['picture']

        # check if the user is in our db
        user = UserModel.find_by_email(data['email'])
        if user is None:
            user = UserModel(None, name, password, email)
            user.save_to_db()

        return user.json()
