from flask import Flask
from flask_restful import Api
from using_resources_endpoints import Users, User

app = Flask(__name__)
api = Api(app)

api.add_resource(Users, '/users')
api.add_resource(User, '/users/<id>')

if __name__ == "__main__":
    app.run(debug = True)