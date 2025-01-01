#users.py

from flask_jwt_extended import get_jwt_identity
from flask import jsonify

# Function to check if the user is an admin
def is_admin():
    current_user = get_jwt_identity()
    if current_user and current_user['role'] == 'admin':
        return True
    return False

# Function to check if the user is a regular user
def is_user():
    current_user = get_jwt_identity()
    if current_user and current_user['role'] == 'user':
        return True
    return False
