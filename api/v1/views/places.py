#!/usr/bin/python3
"""Amenity handlers"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
<<<<<<< HEAD
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
=======
from models.place import Place
from models.city import City


@app_views.route('cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def getPlacesByCity(city_id):
    """get amentiy"""
    ob = storage.all('Place')
    ll = []
    for place in ob.values():
        ll.append(place.to_dict())
    return jsonify(ll)
>>>>>>> 7714ad96c8dff0e17f7d8daa503251e464005968
