from flask import abort, make_response
from config import db
from models import Trail, trails_schema, trail_schema


# Function to read all trails
def read_all():
    trails = Trail.query.all()
    return trails_schema.dump(trails)

# Function to read one trail
def read_one(TrailId):
    trail = Trail.query.filter(Trail.TrailId == TrailId).one_or_none()
    
    if trail is not None:
        return trail_schema.dump(trail)
    else:
        abort(
            404, f"Trail with ID {TrailID} not found"
            )

# Function to update a trail
def update(TrailId, trail):
    existing_trail = Trail.query.filter(Trail.TrailId == TrailId).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.TrailName = update_trail.TrailName
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(
            404,
            f"Trail with ID {TrailId} not found"
            )

# Function to delete a trail
def delete(TrailId):
    existing_trail = Trail.query.filter(Trail.TrailId == TrailId).one_or_none()
    
    if existing_trail:
        db.session.delete(existing_trail)
        db.session.commit()
        return make_response(f"{TrailId} successfully deleted", 200)
    else:
        abort(404, f"Trail with ID {TrailId} not found")
        
        
# Function to create a trail
def create(trail):
    TrailId = trail.get("TrailId")
    existing_trail = Trail.query.filter(Trail.TrailId == TrailId).one_or_none()
    
    if existing_trail is None:
        new_trail = trail_schema.load(trail, session=db.session)
        db.session.add(new_trail)
        db.session.commit()
        return trail_schema.dump(new_trail), 201
    else:
         abort(
            406,
            f"Trail with ID {TrailId} already exists",
            )
            
