from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required, current_identity

from models.post import PostModel


class Post(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True, help='title is required.')

    parser.add_argument('body', type=str, required=True, help='body is required.')

    parser.add_argument('category_id', type=int, required=True, help='Categpry is required.')

    @jwt_required()
    def get(self):
        print(current_identity.id)
        return{'message': 'hey'}

    @jwt_required()
    def delete(self, id):
        # get the current user's id
        user_id = current_identity.id
        post = PostModel.find_by_id(id)

        if post is None:
            return {'success': False, 'message': 'Post was not found'}, 404

        # check if the current user is the owner of the post
        if post.user != user_id:
            return {
                'success': False,
                'message': 'Not Authorized to delete this post'
                }, 401

        # try to delete the post or 500
        try:
            post.delete_from_db()
        except:
            return {'message': 'Something went wrong'}, 500
        return {
            'success': True,
            'message': 'Post was deleted successfully.'
            }, 200

    @jwt_required()
    def put(self, id):
        # get the current user's id
        user_id = current_identity.id
        post = PostModel.find_by_id(id)
        print('here')
        if post is None:
            return {
                'success': False,
                'message': 'Post was not found'
                }, 404

        # check if the current user is the owner of the post
        if post.user != user_id:
            return {
                'success': False,
                'message': 'Not Authorized to Edit this post'
                }, 401

        data = Post.parser.parse_args()
        post.title = data['title']
        post.body = data['body']
        post.category_id = data['category_id']

        # try to delete the post or 500
        try:
            post.save_to_db()
        except:
            return {'message': 'Something went wrong'}, 500
        return {
            'success': True,
            'message': 'Post was edited successfully.'
            }, 200


class AddPost(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True, help='title is required.')

    parser.add_argument('body', type=str, required=True, help='body is required.')

    parser.add_argument('category_id', type=int, required=True, help='Categpry is required.')

    @jwt_required()
    def post(self):
        # get the current user's id
        user_id = current_identity.id
        # get the post data
        data = AddPost.parser.parse_args()
        # Create a new post using the data and user_id
        post = PostModel(None, data['title'], data['body'], user_id, data['category_id'])

        # Try saving the post
        try:
            post.save_to_db()
        except:
            return {'success': False, 'message': 'Something went wrong'}, 500

        return {'sucess': 'Created successfully'}, 201


class ListPosts(Resource):
    @jwt_required()
    def get(self):
        # store current user id
        user_id = current_identity.id
        posts = [post for post in PostModel.query.all()]

        # check to see if the current user is the owner of the post
        for post in posts:
            if post.user == user_id:
                post.owner = True
            else:
                post.owner = False

        return {'posts': [post.json() for post in posts]}
