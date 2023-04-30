#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
view.py file
"""
from flask import jsonify, Blueprint
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """creates a route on app_views that returns JSON"""
    return jsonify({'status': 'OK'})

