#TrailFeatures

from flask import abort, make_response
from config import db
from models import Features, features_schema, feature_schema, Trail, trails_schema, trail_schema, TrailFeature, trailFeature_schema 


# add a feature to a trail
def create(TrailId, FeaturesId):
    trail = Trail.query.get(TrailId)
    if not trail:
        abort(404, f"Trail with id {TrailId} not found")

    feature = Features.query.get(FeaturesId)
    if not feature:
        abort(404, f"Feature with id {FeaturesId} not found")

    # Check if the relationship already exists
    existing_link = TrailFeature.query.filter_by(TrailId=TrailId, FeaturesId=FeaturesId).first()
    if existing_link:
        abort(400, f"Feature {FeaturesId} already linked to trail {TrailId}")

    # Create the new link
    new_link = TrailFeature(TrailId=TrailId, FeaturesId=FeaturesId)
    db.session.add(new_link)
    db.session.commit()

    return {"message": f"Feature {FeaturesId} added to trail {TrailId}"}, 201


# readall features of a specific trail
def read_all(TrailId):
    trail = Trail.query.get(TrailId)
    if not trail:
        abort(404, f"Trail with id {TrailId} not found")

    trail_features = trail.trail_features

    return trailFeature_schema.dump(trail_features, many=True), 200

# delete a feature from a specific trail
def delete(TrailId, FeaturesId):
    existing_trail = Trail.query.get(TrailId)
    if not existing_trail:
        abort(404, f"Trail with id {TrailId} not found")

    trail_feature = TrailFeature.query.filter_by(TrailId=TrailId, FeaturesId=FeaturesId).first()
    if not trail_feature:
        abort(404, f"Feature {FeaturesId} from Trail {TrailId} not found")

    # Delete the TrailFeature relationship
    db.session.delete(trail_feature)
    db.session.commit()

    # Return success message
    return make_response({"message": f"Feature {FeaturesId} from Trail {TrailId} successfully deleted"}, 200)
