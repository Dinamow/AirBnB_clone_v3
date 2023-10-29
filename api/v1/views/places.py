#!/usr/bin/python3
"""Amenity handlers"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
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
