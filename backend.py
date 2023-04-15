from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# //connecting to the database
client = MongoClient('mongodb://localhost:27017/')
db = client['users']

#defining the model of user database
class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password


# creating api's endpoints
# get all the users from the database
@app.route('/users', methods = ['GET'])
def get_users():
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

# get user corresponding to any id
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
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


# //add a user
@app.route('/users', methods=['POST'])
def add_user():
    id = request.json['id']
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    db.users.insert_one({
        'id': id,
        'name': name,
        'email': email,
        'password': password
    })
    return jsonify({"result": 'User added successfully'})


# update the user
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    db.users.update_one({
        "id": id
    },
    {'$set': {
        'name': name,
        'email': email,
        'password': password
    }}
    )
    return jsonify({"result": "User updated successfully"})


@app.route('/users/<id>', methods= ['DELETE'])
def delete_user(id):
    db.users.delete_one({'id': id})
    return jsonify({"result": "User deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)