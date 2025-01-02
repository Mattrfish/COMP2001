from flask import abort, jsonify, request
from flask_jwt_extended import jwt_required, decode_token
from config import db
from models import Trail, trails_schema, trail_schema, User
from utils import role_required
import json


# Function to read all trails (Open to all)
def read_all():
    # Extract token from query parameter
    token = request.args.get("auth")
    if not token:
        return jsonify({"message": "Authorization token required"}), 401

    try:
        # Decode the token manually
        decoded_token = decode_token(token)
        identity = decoded_token.get("sub")  # Extract 'sub' field (user details)
        if not identity:
            return jsonify({"message": "Invalid token"}), 401

       # Parse the 'sub' field as a dictionary
        user_data = json.loads(identity)
        user_id = user_data.get("id")  # Extract the UserID
        role = user_data.get("role")  # Extract the role

        # Verify user exists in the database
        user = User.query.filter_by(UserID=user_id).first()
        if not user:
            return jsonify({"message": "User not found"}), 404

    except Exception as e:
        return jsonify({"message": f"Token decoding error: {str(e)}"}), 401

    # Fetch and return trails (assuming no role restrictions here)
    trails = Trail.query.all()
    return trails_schema.dump(trails), 200

# Function to read one trail (Open to all)
def read_one(TrailId):
    # Extract token from query parameter
    token = request.args.get("auth")
    if not token:
        return jsonify({"message": "Authorization token required"}), 401

    try:
        # Decode the token manually
        decoded_token = decode_token(token)
        identity = decoded_token.get("sub")  # Extract 'sub' field (user details)
        if not identity:
            return jsonify({"message": "Invalid token"}), 401

       # Parse the 'sub' field as a dictionary
        user_data = json.loads(identity)
        user_id = user_data.get("id")  # Extract the UserID
        role = user_data.get("role")  # Extract the role

        # Verify user exists in the database
        user = User.query.filter_by(UserID=user_id).first()
        if not user:
            return jsonify({"message": "User not found"}), 404

    except Exception as e:
        return jsonify({"message": f"Token decoding error: {str(e)}"}), 401
    
    trail = Trail.query.filter(Trail.TrailId == TrailId).one_or_none()
    if trail:
        return trail_schema.dump(trail)
    else:
        abort(404, f"Trail with ID {TrailId} not found")

# Function to update a trail (Admins only)
def update(TrailId, trail):
    # Extract token from query parameter
    token = request.args.get("auth")
    if not token:
        return jsonify({"message": "Authorization token required"}), 401

    try:
        # Decode the token manually
        decoded_token = decode_token(token)
        identity = decoded_token.get("sub")  # Extract 'sub' field (user details)
        if not identity:
            return jsonify({"message": "Invalid token"}), 401

        # Parse the 'sub' field as a dictionary
        user_data = json.loads(identity)
        user_id = user_data.get("id")  # Extract the UserID
        role = user_data.get("role")  # Extract the role

        # Verify user exists in the database
        user = User.query.filter_by(UserID=user_id).first()
        if not user:
            return jsonify({"message": "User not found"}), 404

         # Check if the user has admin role
        if role != "admin":
            return jsonify({"message": "Admin access required"}), 403

    except Exception as e:
        return jsonify({"message": f"Token decoding error: {str(e)}"}), 401
    
    existing_trail = Trail.query.filter(Trail.TrailId == TrailId).one_or_none()
    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.TrailName = update_trail.TrailName
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f"Trail with ID {TrailId} not found")

# Function to delete a trail (Admins only)
def delete(TrailId):
    # Extract token from query parameter
    token = request.args.get("auth")
    if not token:
        return jsonify({"message": "Authorization token required"}), 401

    try:
        # Decode the token manually
        decoded_token = decode_token(token)
        identity = decoded_token.get("sub")  # Extract 'sub' field (user details)
        if not identity:
            return jsonify({"message": "Invalid token"}), 401

       # Parse the 'sub' field as a dictionary
        user_data = json.loads(identity)
        user_id = user_data.get("id")  # Extract the UserID
        role = user_data.get("role")  # Extract the role

        # Verify user exists in the database
        user = User.query.filter_by(UserID=user_id).first()
        if not user:
            return jsonify({"message": "User not found"}), 404

         # Check if the user has admin role
        if role != "admin":
            return jsonify({"message": "Admin access required"}), 403

    except Exception as e:
        return jsonify({"message": f"Token decoding error: {str(e)}"}), 401
    
    existing_trail = Trail.query.filter(Trail.TrailId == TrailId).one_or_none()
    if existing_trail:
        db.session.delete(existing_trail)
        db.session.commit()
        return jsonify({"message": f"{TrailId} successfully deleted"}), 200
    else:
        abort(404, f"Trail with ID {TrailId} not found")

# Function to create a trail (Admins only)
def create(trail):
    # Extract token from query parameter
    token = request.args.get("auth")
    if not token:
        return jsonify({"message": "Authorization token required"}), 401

    try:
        # Decode the token manually
        decoded_token = decode_token(token)
        identity = decoded_token.get("sub")  # Extract 'sub' field (user details)
        if not identity:
            return jsonify({"message": "Invalid token"}), 401

       # Parse the 'sub' field as a dictionary
        user_data = json.loads(identity)
        user_id = user_data.get("id")  # Extract the UserID
        role = user_data.get("role")  # Extract the role

        # Verify user exists in the database
        user = User.query.filter_by(UserID=user_id).first()
        if not user:
            return jsonify({"message": "User not found"}), 404

         # Check if the user has admin role
        if role != "admin":
            return jsonify({"message": "Admin access required"}), 403

    except Exception as e:
        return jsonify({"message": f"Token decoding error: {str(e)}"}), 401
    
    TrailId = trail.get("TrailId")
    existing_trail = Trail.query.filter(Trail.TrailId == TrailId).one_or_none()
    if existing_trail is None:
        new_trail = trail_schema.load(trail, session=db.session)
        db.session.add(new_trail)
        db.session.commit()
        return trail_schema.dump(new_trail), 201
    else:
        abort(406, f"Trail with ID {TrailId} already exists")
