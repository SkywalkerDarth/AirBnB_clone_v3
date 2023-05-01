#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
users.py file
"""
from flask import jsonify, abort, make_response, request
from models.user import User
from models import storage
from api.v1.views import app_views

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def users():
    """ Retrieve list of all Users objects """
    rl_users = storage.all(Users)
    return jsonify([obj.to_dict() for obj in rl_users.values()])

@app_views.route('/users/<user_id>', methods=['GET'], 
                 strict_slashes=False)
def get_obj_user_id(user_id):
    """ Retrieve a Users object """
    user = storage.get("Users", user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())

@app_views.route('/users/<user_id>', methods=['DELETE'], 
                 strict_slashes=False)
def delete_user(user_id):
    """ Delete a Users object """
    user = storage.get("Users", user_id)
    if not user:
        abort(404)
    user.delete()
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """ Post a Users object """
    new_user = request.get_json()
    if not new_user:
        abort(400, "Not a JSON")
    if "name" not in new_user:
        abort(400, "Missing name")
    user = Users(**new_user)
    storage.new(user)
    storage.save()
    return make_response(jsonify(user.to_dict()), 201)

@app_views.route('/users/<user_id>',  strict_slashes=False)
def put_user(user_id):
    """ Updates a Users object """
    user = storage.get("Users", user_id)
    if not user:
        abort(404)
    body_request = request.get_json()
    if not body_request:
        abort(400, "Not a JSON")
    for k, v in body_request.items():
        if k != 'id' and k != 'created_at' and k != 'updated_at':
            setattr(user, k, v)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)
