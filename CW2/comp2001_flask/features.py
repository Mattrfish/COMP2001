from flask import abort, make_response

from config import db
from models import Features, features_schema, feature_schema

# Function to read all features
def read_all():
    features = Features.query.all()
    return features_schema.dump(features)

# Function to read one feature
def read_one(FeaturesId):
    features = Features.query.filter(Features.FeaturesId == FeaturesId).one_or_none()

    if features is not None:
        return feature_schema.dump(features)
    else:
        abort(
            404, f"Feature with ID {FeaturesId} not found"
        )

# Function to delete a feature
def delete(FeaturesId):
    existing_feature = Features.query.filter(Features.FeaturesId == FeaturesId).one_or_none()

    if existing_feature:
        db.session.delete(existing_feature)
        db.session.commit()
        return make_response({"message": f"Feature with ID {FeaturesId} successfully deleted"}, 200)
    else:
        abort(404, f"Feature with ID {FeaturesId} not found")

# Function to create a feature
def create(features):
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
