from flask_restful import Resource, reqparse
from pymongo import MongoClient
from flask import jsonify

client = MongoClient('mongodb://localhost:27017')
db = client['users']

class Users(Resource):
    def get(self):
        users = db.users.find()
        output = []
        for user in users:
            output.append({
                'id': user['id'],
                'name': user['name'],
                'email': user['email'],
                'password': user['password']
            })
        return jsonify({'result': output})
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', required = True)
        parser.add_argument('name', required = True)
        parser.add_argument('email', required = True)
        parser.add_argument('password', required = True)
        args = parser.parse_args()

        db.users.insert_one({
            'id': args['id'],
            'name': args['name'],
            'email': args['email'],
            'password': args['password']
        })
        return {'result': 'User added successfully'}

class User(Resource):
    def get(self, id):
        user = db.users.find_one({'id': id})
        if user:
            output = {
                'id': user['id'],
                'name': user['name'],
                'email': user['email'],
                'password': user['password']
            }
        else:
            output = 'User not found'
        return jsonify({'result': output})
    
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('email', required = True)
        parser.add_argument('password', required=True)
        args = parser.parse_args()

        db.users.update_one({'id': id},
        {
            '$set': {
                'name': args['name'],
                'email': args['email'],
                'password': args['password']
            }
        })
        return {'result': 'User updated successfully'}

    def delete(self, id):
        db.users.delete_one({'id': id})
        return {'result': 'User deleted successfully'}