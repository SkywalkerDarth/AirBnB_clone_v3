#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
view.py file
"""
from models.state import State
from flask import jsonify, Blueprint
from api.v1.views import app_views
from models import Storage

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """creates a route on app_views that returns JSON"""
    return jsonify({'status': 'OK'})

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def object_status():
    """Creates an endpoint, retrieves number of each object by type"""
    objects = {"amenities": 'Amenity', "cities": 'City',
               "places": 'Place', "reviews": 'Review',
               "states": 'State', "users": 'User'}
    for key, value in objects.items():
        objects[key] = storage.count(value)
    return jsonify(objects)
