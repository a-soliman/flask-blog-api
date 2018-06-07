from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required, current_identity

from models.category import CategoryModel


class Category(Resource):
    def get(self, name):
        category = CategoryModel.find_by_name(name)

        if category is None:
            return {'success': False, 'message': 'Category was not found'}, 404
        return category.json(), 200

    def post(self, name):
        if CategoryModel.find_by_name(name):
            return {
                'success': False,
                'message': 'A category with this name already exists'
                }, 400

        category = CategoryModel(None, name)

        # try to save
        try:
            category.save_to_db()
        except:
            return {
                'success': False,
                'message': 'Something went wrong'
                }, 500

        return {
            'success': True,
            'message': 'A category was successfully created'
            }, 201

    def delete(self, name):
        category = CategoryModel.find_by_name(name)
        if category is None:
            return {
                'success': False,
                'message': 'Category was not found.'
                }, 404

        # try to delete
        try:
            category.delete_from_db()
        except:
            return{
                'success': False,
                'message': 'Something went wrong.'
                }, 500
        return {
            'success': True,
            'message': 'Category was successfully deleted.'
            }, 200


class CategoryList(Resource):
    def get(self):
        return {
            'categories': [category.json() for category in CategoryModel.query.all()]
            }
