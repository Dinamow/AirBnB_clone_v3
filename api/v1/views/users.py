#!/usr/bin/python3
"""Amenity handlers"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.user import User


@app_views.route('users', methods=['GET'],
                 strict_slashes=False)
def getUser():
    """get user"""
    ob = storage.all('User')
    ll = []
    for state in ob.values():
        ll.append(state.to_dict())
    return jsonify(ll)


@app_views.route('users/<user_id>', methods=['GET'],
                 strict_slashes=False)
def getUserById(user_id):
    """user amentiy"""
    element = storage.get(User, user_id)
    if element:
        return jsonify(element.to_dict())
    else:
        abort(404)


@app_views.route('users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def DeleteAmentiyById(user_id):
    """delete amentiy"""
    element = storage.get(User, user_id)
    if not element:
        abort(404)
    else:
        storage.delete(element)
        storage.save()
        return (jsonify({}), 200)


@app_views.route('users', methods=['POST'],
                 strict_slashes=False)
def CreateUser():
    """Post user"""
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"error": "Not a JSON"}), 400
    if "email" not in data:
        return jsonify({"error": "Missing email"}), 400
    if "password" not in data:
        return jsonify({"error": "Missing password"}), 400
    user = User(email=data["email"], password=data['password'])
    storage.new(user)
    storage.save()


@app_views.route('users/<user_id>', methods=['POST'],
                 strict_slashes=False)
def UpdateUser(user_id):
    """Update user"""
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"error": "Not a JSON"}), 400
    user = storage.get(User, user_id)
    if not user_id:
        abort(404)
    else:
        ignoreKeys = ['id', 'created_at', 'updated_at']
        for key, val in data.items():
            if key not in ignoreKeys:
                setattr(user, key, val)
        storage.save()
        return jsonify(user.to_dict()), '200'
