#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Api upgrade
"""
from os import getenv
from flask import Flask, jsonify, Blueprint
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)



@app.teardown_appcontext
def close_db_session(error):
    """ slash routing"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """ Returns 404 status """
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    HBNB_API_HOST = getenv('HBNB_API_HOST')
    HBNB_API_PORT = getenv('HBNB_API_PORT')
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True, debug=True)
