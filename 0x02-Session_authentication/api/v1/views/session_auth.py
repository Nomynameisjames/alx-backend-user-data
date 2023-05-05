#!/usr/bin/env python3
"""
    import files
"""
import os
from flask import Flask, jsonify, request, abort
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
        user login logic implementation
    """
    email = request.form.get('email')
    if email is None:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if password is None:
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if user.is_valid_password(password) is False:
            return jsonify({"error": "wrong password"}), 401
        from api.v1.app import auth
        session_id = auth.create_session(user.id)
        cookie_name = os.getenv('SESSION_NAME')
        cookie_path = '/'
        cookie_value = session_id
        response = jsonify(user.to_json())
        response.set_cookie(cookie_name, cookie_value, path=cookie_path)
        return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """
        user logout logic implementation
    """
    from api.v1.app import auth
    if auth.destroy_session(request) is False:
        abort(404)
    else:
        return jsonify({}), 200
