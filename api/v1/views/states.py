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
    """ Retrieves a State object """
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())

@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """ Deletes a State object """
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
def get_state_id(state_id):
    """ returns state obj with specific  od"""
    state = storage.get('State', state_id)
    if state is None:
        abort(404)
    elif request.method == 'GET':
        return jsonify(state.to_dict())
    elif request.method == 'DELETE':
        state = storage.get('State', state_id)
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    elif request.method == 'PUT':
        put = request.get_json()
        if put is None or type(put) != dict:
            return jsonify({'error': 'Not a JSON'}), 400
        for key, value in put.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(state, key, value)
                storage.save()
        return jsonify(state.to_dict()), 200
