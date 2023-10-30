#!/usr/bin/python3
"""comment for city ile"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.city import City


@app_views.route('/states/<string:state_id>/cities', methods=['GET']
                 strict_slashes=False)
def CitiesBySateId(state_id):
    """get cities by state id"""
    cities = storage.all('City')
    ll = []
    for x in cities.values():
        if x.state_id == state_id:
            ll.append(x.to_dict())
    if len(ll) <= 0:
        abort(404)
    return jsonify(ll), 200


@app_views.route('/cities/<string:city_id>/', methods=['GET']
                 strict_slashes=False)
def getCityById(city_id):
    """get city by id"""
    x = storage.get(City, city_id)
    if x is None:
        abort(404)
    return jsonify(x.to_dict()), 200


@app_views.route('/cities/<string:city_id>/', methods=['DELETE']
                 strict_slashes=False)
def deletecity(city_id):
    """deletes city by id"""
    x = storage.get(City, city_id)
    if x is None:
        abort(404)
    storage.delete(x)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<string:city_id>/', methods=['PUT']
                 strict_slashes=False)
def updatecity(city_id):
    """put city"""
    response = request.get_json()
    if not response:
        abort(400, {'Not a JSON'})
    if not response.get('name'):
        abort(400, {'Missing name'})
    stateObject = storage.get(City, city_id)
    if not stateObject:
        abort(404)
    ignoreKeys = ['id', 'created_at', 'updated_at']
    for key, val in response.items():
        if key not in ignoreKeys:
            setattr(stateObject, key, val)
    storage.save()
    return jsonify(stateObject.to_dict()), '200'


@app_views.route('/states/<string:state_id>/cities/', methods=['POST']
                 strict_slashes=False)
def createcity(state_id):
    """post city"""
    response = request.get_json()
    if not response:
        abort(400, {'Not a JSON'})
    if not response.get('name'):
        abort(400, {'Missing name'})
    stateObject = City(**response)
    storage.new(stateObject)
    storage.save()
    return jsonify(stateObject.to_dict()), '201'
