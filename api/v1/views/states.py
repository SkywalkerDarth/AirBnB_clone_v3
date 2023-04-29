#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
states.py file
"""
from flask import Blueprint, jsonify, request, abort
from models.state import State
from models import storage
from api.v1.views import app_views

@app_views.route('/states' methods=['GET', 'POST'], strict_slashes=False)
def states():

