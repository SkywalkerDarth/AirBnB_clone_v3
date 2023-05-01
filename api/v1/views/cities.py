#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
cities.py file
"""
from flask import jsonify, abort, make_response, request
from models.state import State
from models import storage
from api.v1.views import app_viewsi
from models.city import City

@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def cities(state_id):
    """ retrieves list of all city objects """
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    return jsonify([city.to_dict() for city in state.cities()])

@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def Rtr_city_id(city_id):
    """ Retrieve a City object """
    city = storage.get("City", city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())

@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_city(city_id):
    """ Delete a City object """
    city = storage.get("City", city_id)
    if not city:
        abort(404)
    city.delete()
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    """ Post a city object """
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    new_city = request.get_json()
    if not new_city:
        abort(400, "Not a JSON")
    if "name" not in new_city:
        abort(400, "Missing name")
    city = City(**new_city)
    setattr(city, 'state_id', state_id)
    storage.new(city)
    storage.save()
    return make_response(jsonify(city.to_dict()), 201)

@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def put_city(state_id):
    """ Update a City object """
    city = storage.get("City", city_id)
    if not city:
        abort(404)
    body_req = request.get_json()
    if not body_req:
        abort(400, "Not a JSON")

    for k, v in body_req.items():
        if k not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(city, k, v)

    storage.save()
    return make_response(jsonify(city.to_dict()), 200)
