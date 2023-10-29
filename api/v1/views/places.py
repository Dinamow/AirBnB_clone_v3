#!/usr/bin/python3
"""comment for file"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.city import City
from models.place import Place


@app_views.route('/cities/<string:city_id>/places', methods=['GET'], strict_slashes=False)
def listofplaces(city_id):
    """comment for func"""
    ob = storage.all('Place')
    ll = []
    for place in ob.values():
        if place.to_dict()['city_id'] == city_id:
            ll.append(place)
    if len(ll) <= 0:
        abort(404)
    return jsonify(ll), 200
