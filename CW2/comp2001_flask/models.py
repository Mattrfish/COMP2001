#models.py

import pytz
from config import db, ma

class Trail(db.Model):
    __tablename__ = "Trail"
    __table_args__ = {'schema' : 'CW2' } 
    

    TrailId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    TrailName = db.Column(db.String(50), nullable=False)
    TrailSummary = db.Column(db.String(500), nullable=True)
    TrailDescription = db.Column(db.String(500), nullable=True)
    Difficulty = db.Column(db.String(8), nullable=False)
    Location = db.Column(db.String(100), nullable=False)
    Length = db.Column(db.Numeric(8, 2), nullable=False)
    ElevationGain = db.Column(db.Numeric(6, 2), nullable=False)
    RouteType = db.Column(db.String(25), nullable=False)
    OwnerID = db.Column(db.Integer, nullable=False)
    
    Pt1_Lat = db.Column(db.Numeric(9, 6), nullable=True)
    Pt1_Long = db.Column(db.Numeric(9, 6), nullable=True)
    Pt1_Desc = db.Column(db.String(200), nullable=True)
    
    Pt2_Lat = db.Column(db.Numeric(9, 6), nullable=True)
    Pt2_Long = db.Column(db.Numeric(9, 6), nullable=True)
    Pt2_Desc = db.Column(db.String(200), nullable=True)
    
    Pt3_Lat = db.Column(db.Numeric(9, 6), nullable=True)
    Pt3_Long = db.Column(db.Numeric(9, 6), nullable=True)
    Pt3_Desc = db.Column(db.String(200), nullable=True)
    
    Pt4_Lat = db.Column(db.Numeric(9, 6), nullable=True)
    Pt4_Long = db.Column(db.Numeric(9, 6), nullable=True)
    Pt4_Desc = db.Column(db.String(200), nullable=True)
    
    Pt5_Lat = db.Column(db.Numeric(9, 6), nullable=True)
    Pt5_Long = db.Column(db.Numeric(9, 6), nullable=True)
    Pt5_Desc = db.Column(db.String(200), nullable=True)


class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        load_instance = True
        sql_session = db.session

trail_schema = TrailSchema()
trails_schema = TrailSchema(many=True)
