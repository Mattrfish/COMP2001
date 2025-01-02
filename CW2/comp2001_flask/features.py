from flask import abort, make_response, jsonify, request
from config import db
from models import Features, features_schema, feature_schema, User
import json
from flask_jwt_extended import jwt_required, decode_token

# Function to read all features
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
    features = Features.query.all()
    return features_schema.dump(features)

# Function to read one feature
def read_one(FeaturesId):
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
    
    features = Features.query.filter(Features.FeaturesId == FeaturesId).one_or_none()

    if features is not None:
        return feature_schema.dump(features)
    else:
        abort(
            404, f"Feature with ID {FeaturesId} not found"
        )

# Function to delete a feature
def delete(FeaturesId):
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


    existing_feature = Features.query.filter(Features.FeaturesId == FeaturesId).one_or_none()

    if existing_feature:
        db.session.delete(existing_feature)
        db.session.commit()
        return make_response({"message": f"Feature with ID {FeaturesId} successfully deleted"}, 200)
    else:
        abort(404, f"Feature with ID {FeaturesId} not found")

# Function to create a feature
def create(features):
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


    FeaturesId = features.get("FeaturesId")
    existing_feature = Features.query.filter(Features.FeaturesId == FeaturesId).one_or_none()

    if existing_feature is None:
        new_feature = feature_schema.load(features, session=db.session)
        db.session.add(new_feature)
        db.session.commit()
        return feature_schema.dump(new_feature), 201
    else:
        abort(
            406,
            f"Feature with ID {FeaturesId} already exists"
        )

# function to update a feature
def update (FeaturesId, features):
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


    existing_feature = Features.query.filter(Features.FeaturesId == FeaturesId).one_or_none()

    if existing_feature:
        update_feature = feature_schema.load(features, session=db.session)
        existing_feature.Feature = update_feature.Feature
        db.session.merge(existing_feature)
        db.session.commit()
        return feature_schema.dump(existing_feature), 201
    else:
        abort(
            404,
            f"Feature with id {FeaturesId} not found"
            )
