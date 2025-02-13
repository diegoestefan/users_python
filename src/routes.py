from flask import request, jsonify, Response
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util, ObjectId
from bson.errors import InvalidId

def get_mongo():
    from flask import current_app
    return current_app.mongo

def create_user():
    """
        Create new user.
        ---
        tags:
          - Users
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              required:
                - username
                - password
                - email
              properties:
                username:
                  type: string
                  description: Username
                password:
                  type: string
                  description: Password
                email:
                  type: string
                  description: E-mail
        responses:
          201:
            description: User created successfully
          400:
            description: Bad request
    """
    data = request.get_json()
    if not data or not all(k in data for k in ('username', 'password', 'email')):
        return jsonify({'error': 'Missing fields'}), 400

    hashed_password = generate_password_hash(data['password'])
    user_id = get_mongo().db.users.insert_one({
        'username': data['username'],
        'password': hashed_password,
        'email': data['email']
    }).inserted_id

    return jsonify({'id': str(user_id), 'username': data['username'], 'email': data['email']}), 201

def get_users():
    """
     Get list of users.
     ---
     tags:
       - Users
     responses:
       200:
         description: List of users
         schema:
           type: array
           items:
             type: object
             properties:
               _id:
                 type: string
                 description: User ID
               username:
                 type: string
                 description: Username
               email:
                 type: string
                 description: User email
       500:
         description: Internal server error
     """
    users = get_mongo().db.users.find()
    return Response(json_util.dumps(users), mimetype='application/json')

def get_user(id):
    """
    Get a user by ID.
    ---
    tags:
      - Users
    parameters:
      - name: id
        in: path
        required: true
        description: The ID of the user to retrieve
        type: string
    responses:
      200:
        description: User found
        schema:
          type: object
          properties:
            _id:
              type: string
              description: User ID
            username:
              type: string
              description: Username
            email:
              type: string
              description: User email
      400:
        description: Invalid ID format
      404:
        description: User not found
    """
    try:
        user = get_mongo().db.users.find_one({'_id': ObjectId(id)})
        if not user:
            return jsonify({'error': 'User not found'}), 404
        return Response(json_util.dumps(user), mimetype='application/json')
    except InvalidId:
        return jsonify({'error': 'Invalid ID format'}), 400

def delete_user(id):
    """
    Delete a user by ID.
    ---
    tags:
      - Users
    parameters:
      - name: id
        in: path
        required: true
        description: The ID of the user to delete
        type: string
    responses:
      200:
        description: User deleted successfully
      400:
        description: Invalid ID format
      404:
        description: User not found
    """
    try:
        result = get_mongo().db.users.delete_one({'_id': ObjectId(id)})
        if result.deleted_count == 0:
            return jsonify({'error': 'User not found'}), 404
        return jsonify({'message': f'User {id} was deleted successfully'}), 200
    except InvalidId:
        return jsonify({'error': 'Invalid ID format'}), 400

def update_user(id):
    """
    Update a user's information.
    ---
    tags:
      - Users
    parameters:
      - name: id
        in: path
        required: true
        description: The ID of the user to update
        type: string
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - username
            - password
            - email
          properties:
            username:
              type: string
              description: Username
            password:
              type: string
              description: Password
            email:
              type: string
              description: E-mail
    responses:
      200:
        description: User updated successfully
      400:
        description: Missing fields or invalid ID format
      404:
        description: User not found
    """
    data = request.get_json()
    if not data or not all(k in data for k in ('username', 'password', 'email')):
        return jsonify({'error': 'Missing fields'}), 400

    hashed_password = generate_password_hash(data['password'])
    try:
        result = get_mongo().db.users.update_one({'_id': ObjectId(id)}, {'$set': {
            'username': data['username'],
            'password': hashed_password,
            'email': data['email']
        }})
        if result.matched_count == 0:
            return jsonify({'error': 'User not found'}), 404
        return jsonify({'message': f'User {id} was updated successfully'}), 200
    except InvalidId:
        return jsonify({'error': 'Invalid ID format'}), 400
