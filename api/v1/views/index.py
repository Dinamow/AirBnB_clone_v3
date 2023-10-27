#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', strict_slashes=False)
def statusok():
    """status home page"""
    return jsonify(status='OK'), 200