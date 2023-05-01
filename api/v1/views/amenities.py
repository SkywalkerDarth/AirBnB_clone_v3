#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
amenities.py file
"""
from flask import jsonify, abort, make_response, request
from models.amenity import Amenity
from models import storage
from api.v1.views import app_views

@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def amenities():
    """ retrieves list of all amenity objects """
    d_amenities = storage.all(Amenity)
    return jsonify([obj.to_dict() for obj in d_amenities.values()])

@app_views.route('/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def object_amenity_id(amenity_id):
    """ Retrieve an amenity object """
    amenity = storage.get("Amenity", amenity_id)
    if not amenity:
        abort(404)
    return jsonify(amenity.to_dict())

@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    """ Delete amenity object """
    amenity = storage.get("Amenity", amenity_id)
    if not amenity:
        abort(404)
    amenity.delete()
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/amenities', methods=['POST'], strict_slashes=False)

def post_amenity():
    """ Post amenity object """
    new_amenity = request.get_json()
    if not new_amenity:
        abort(400, "Not a JSON")
    if "name" not in new_amenity:
        abort(400, "Missing name")
    amenity = Amenity(**new_amenity)
    storage.new(amenity)
    storage.save()
    return make_response(jsonify(amenity.to_dict()), 201)

@app_views.route('/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def put_amenity(amenity_id):
    """ Update amenity object """
    amenity = storage.get("Amenity", amenity_id)
    if not amenity:
        abort(404)
    body_req = request.get_json()
    if not body_req:
        abort(400, "Not a JSON")

    for k, v in body_req.items():
        if k != 'id' and k != 'created_at' and k != 'updated_at':
            setattr(amenity, k, v)

    storage.save()
    return make_response(jsonify(amenity.to_dict()), 200)
