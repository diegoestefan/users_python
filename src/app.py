from flask import Flask, jsonify
from flask_pymongo import PyMongo
from routes import create_user, get_users, get_user, delete_user, update_user
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/python'

mongo = PyMongo(app)
app.mongo = mongo

@app.route("/swagger")
def swagger_docs():
    swag = swagger(app)
    swag['info'] = {
        "title": "User API",
        "version": "1.0",
        "description": "User API documentation using Flask-Swagger"
    }
    return jsonify(swag)

SWAGGER_URL = "/docs"
API_URL = "/swagger"

swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

app.add_url_rule('/users', 'create_user', create_user, methods=['POST'])
app.add_url_rule('/users', 'get_users', get_users, methods=['GET'])
app.add_url_rule('/users/<id>', 'get_user', get_user, methods=['GET'])
app.add_url_rule('/users/<id>', 'delete_user', delete_user, methods=['DELETE'])
app.add_url_rule('/users/<id>', 'update_user', update_user, methods=['PUT'])

if __name__ == "__main__":
    app.run(debug=True)
