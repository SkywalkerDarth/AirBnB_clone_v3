#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
states.py file
"""
from flask import jsonify, abort, make_response, request
from models.state import State
from models import storage
from api.v1.views import app_views

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """ retrieves list of all state objects """
    d_states = storage.all(State)
    return jsonify([obj.to_dict() for obj in d_states.values()])

@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def object_state_id(state_id):
    """ Retrieve a State object """
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())

@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """ Delete a State object """
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    state.delete()
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/states', methods=['POST'], strict_slashes=False)

def post_state():
    """ Post a State object """
    new_state = request.get_json()
    if not new_state:
        abort(400, "Not a JSON")
    if "name" not in new_state:
        abort(400, "Missing name")
    state = State(**new_state)
    storage.new(state)
    storage.save()
    return make_response(jsonify(state.to_dict()), 201)

@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """ Update a State object """
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    body_req = request.get_json()
    if not body_req:
        abort(400, "Not a JSON")

    for k, v in body_req.items():
        if k != 'id' and k != 'created_at' and k != 'updated_at':
            setattr(state, k, v)

    storage.save()
    return make_response(jsonify(state.to_dict()), 200)
