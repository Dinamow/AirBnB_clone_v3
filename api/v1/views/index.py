#!/usr/bin/python3
"""the index file"""
from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', strict_slashes=False)
def statusok():
    """status home page"""
    return jsonify(status='OK'), 200

@app_views.route('/stats', strict_slashes=False)
def statssok():
    """stats home page"""
    data = {"amenities" : storage.count()}
    return jsonify(data), 200
