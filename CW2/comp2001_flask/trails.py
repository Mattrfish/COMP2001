from datetime import datetime
from flask import abort, make_response
# Function to generate timestamp
def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Simulating a collection of trails as a dictionary
TRAILS = {
    1: {
        "TrailId": 1,
        "TrailName": "Sunset Trail",
        "TrailSummary": "A scenic trail with views of the sunset.",
        "TrailDescription": "This trail offers beautiful views of the sunset over the mountains. It is a moderately difficult hike.",
        "Difficulty": "Moderate",
        "Location": "Sunset Park",
        "Length": 5.2,
        "ElevationGain": 300.5,
        "RouteType": "Loop",
        "OwnerID": 101,
        "Pt1_Lat": 40.712776,
        "Pt1_Long": -74.005974,
        "Pt1_Desc": "Starting point at the park entrance.",
        "Pt2_Lat": 40.715776,
        "Pt2_Long": -74.003974,
        "Pt2_Desc": "The first view spot.",
        "Pt3_Lat": 40.718776,
        "Pt3_Long": -74.000974,
        "Pt3_Desc": "The summit viewpoint.",
        "Pt4_Lat": 40.720776,
        "Pt4_Long": -73.998974,
        "Pt4_Desc": "The final descent.",
        "Pt5_Lat": 40.722776,
        "Pt5_Long": -73.997974,
        "Pt5_Desc": "Return to the park entrance."
    },
    2: {
        "TrailId": 2,
        "TrailName": "Mountain Peak Trail",
        "TrailSummary": "A challenging trail to reach the mountain peak.",
        "TrailDescription": "This is a challenging trail that takes you to the peak of the mountain, offering breathtaking panoramic views.",
        "Difficulty": "Hard",
        "Location": "Mountain National Park",
        "Length": 9.8,
        "ElevationGain": 1200.5,
        "RouteType": "Out and Back",
        "OwnerID": 102,
        "Pt1_Lat": 35.6762,
        "Pt1_Long": 139.6503,
        "Pt1_Desc": "Trailhead at the base of the mountain.",
        "Pt2_Lat": 35.6782,
        "Pt2_Long": 139.6533,
        "Pt2_Desc": "The first steep section.",
        "Pt3_Lat": 35.6802,
        "Pt3_Long": 139.6563,
        "Pt3_Desc": "A plateau with panoramic views.",
        "Pt4_Lat": 35.6822,
        "Pt4_Long": 139.6593,
        "Pt4_Desc": "The final ascent to the peak.",
        "Pt5_Lat": 35.6842,
        "Pt5_Long": 139.6623,
        "Pt5_Desc": "Reach the summit and enjoy the view."
    },
    3: {
        "TrailId": 3,
        "TrailName": "River Walk",
        "TrailSummary": "A peaceful walk along the river.",
        "TrailDescription": "This easy trail takes you along a calm river, perfect for a relaxing walk.",
        "Difficulty": "Easy",
        "Location": "Riverfront Park",
        "Length": 2.3,
        "ElevationGain": 50.0,
        "RouteType": "Loop",
        "OwnerID": 103,
        "Pt1_Lat": 34.052235,
        "Pt1_Long": -118.243683,
        "Pt1_Desc": "Start at the riverbank near the park.",
        "Pt2_Lat": 34.054235,
        "Pt2_Long": -118.241683,
        "Pt2_Desc": "The halfway point near a small bridge.",
        "Pt3_Lat": 34.056235,
        "Pt3_Long": -118.239683,
        "Pt3_Desc": "Pass by a small waterfall.",
        "Pt4_Lat": 34.058235,
        "Pt4_Long": -118.237683,
        "Pt4_Desc": "Final stretch back to the starting point.",
        "Pt5_Lat": 34.060235,
        "Pt5_Long": -118.235683,
        "Pt5_Desc": "End of the trail at the park entrance."
    }
}

# Function to read all trails
def read_all():
    return list(TRAILS.values())

# Function to read one trail
def read_one(TrailId):
    if TrailId in TRAILS:
        return TRAILS[TrailId]
    else:
        abort(
            404, f"Trail with ID {TrailID} not found"
            )

# Function to update a trail
def update(TrailId, trail):
    if TrailId in TRAILS:
        TRAILS[TrailId]["TrailName"] = trail.get("TrailName", TRAILS[TrailId]["TrailName"])
        TRAILS[TrailId]["timestamp"] = get_timestamp()
        returnTRAILS[TrailId]
    else:
        abort(
            404,
            f"Trail with ID {TrailId} not found"
            )

# Function to delete a trail
def delete(TrailId):
    if TrailId in TRAILS:
        del TRAILS[TrailId]
        return make_response(
            f"{TrailId} successfully deleted", 200
            )
    else:
        abort(
            404,
            f"Trail with ID {TrailId} not found"
            )
        
        
# Function to create a trail
def create(trail):
    TrailId = trail.get("TrailId")

    # Ensure that TrailId is not already in use
    if TrailId in TRAILS:
        abort(406, f"Trail with ID {TrailId} already exists.")
    
    # Add the new trail to the TRAILS dictionary
    TRAILS[trail_id] = {
        "TrailId": TrailId,
        "TrailName": trail.get("TrailName"),
        "TrailSummary": trail.get("TrailSummary"),
        "TrailDescription": trail.get("TrailDescription"),
        "Difficulty": trail.get("Difficulty"),
        "Location": trail.get("Location"),
        "Length": trail.get("Length"),
        "ElevationGain": trail.get("ElevationGain"),
        "RouteType": trail.get("RouteType"),
        "OwnerID": trail.get("OwnerID"),
        "Pt1_Lat": trail.get("Pt1_Lat"),
        "Pt1_Long": trail.get("Pt1_Long"),
        "Pt1_Desc": trail.get("Pt1_Desc"),
        "Pt2_Lat": trail.get("Pt2_Lat"),
        "Pt2_Long": trail.get("Pt2_Long"),
        "Pt2_Desc": trail.get("Pt2_Desc"),
        "Pt3_Lat": trail.get("Pt3_Lat"),
        "Pt3_Long": trail.get("Pt3_Long"),
        "Pt3_Desc": trail.get("Pt3_Desc"),
        "Pt4_Lat": trail.get("Pt4_Lat"),
        "Pt4_Long": trail.get("Pt4_Long"),
        "Pt4_Desc": trail.get("Pt4_Desc"),
        "Pt5_Lat": trail.get("Pt5_Lat"),
        "Pt5_Long": trail.get("Pt5_Long"),
        "Pt5_Desc": trail.get("Pt5_Desc"),
        "Timestamp": get_timestamp()
    }

    return TRAILS[TrailId], 201
