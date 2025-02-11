from flask import Flask
from flask_pymongo import PyMongo
from routes import create_user, get_users, get_user, delete_user, update_user

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/python'

mongo = PyMongo(app)
app.mongo = mongo

app.add_url_rule('/users', 'create_user', create_user, methods=['POST'])
app.add_url_rule('/users', 'get_users', get_users, methods=['GET'])
app.add_url_rule('/users/<id>', 'get_user', get_user, methods=['GET'])
app.add_url_rule('/users/<id>', 'delete_user', delete_user, methods=['DELETE'])
app.add_url_rule('/users/<id>', 'update_user', update_user, methods=['PUT'])

if __name__ == "__main__":
    app.run(debug=True)
