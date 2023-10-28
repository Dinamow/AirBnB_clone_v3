#!/usr/bin/python3
"""Amenity handlers"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.amenity import Amenity


@app_views.route('amenities', methods=['GET'],
                 strict_slashes=False)
def getAmentiy():
    """get amentiy"""
    ob = storage.all('Amenity')
    ll = []
    for state in ob.values():
        ll.append(state.to_dict())
    return jsonify(ll)


@app_views.route('amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def getAmentiyById(amenity_id):
    """get amentiy"""
    element = storage.get(Amenity, amenity_id)
    if element:
        return jsonify(element.to_dict())
    else:
        abort(404)


@app_views.route('amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def DeleteAmentiyById(amenity_id):
    """delete amentiy"""
    element = storage.get(Amenity, amenity_id)
    if not element:
        abort(404)
    else:
        storage.delete(element)
        storage.save()
        return (jsonify({}), 200)


@app_views.route('amenities', methods=['POST'],
                 strict_slashes=False)
def CreateAmenity():
    """Post amentiy"""
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"error": "Not a JSON"}), 400
    if "name" not in data:
        return jsonify({"error": "Missing name"}), 400
    amenity = Amenity(name=data["name"])
    storage.new(amenity)
    storage.save()


@app_views.route('amenities/<amenity_id>', methods=['POST'],
                 strict_slashes=False)
def UpdateAmenity(amenity_id):
    """Update amentiy"""
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"error": "Not a JSON"}), 400
    amenity = storage.get(Amenity, amenity_id)
    if not amenity_id:
        abort(404)
    else:
        ignoreKeys = ['id', 'created_at', 'updated_at']
        for key, val in data.items():
            if key not in ignoreKeys:
                setattr(amenity, key, val)
        storage.save()
        return jsonify(amenity.to_dict()), '200'
