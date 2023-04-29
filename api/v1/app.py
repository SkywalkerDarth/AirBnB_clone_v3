#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Api upgrade
"""
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


