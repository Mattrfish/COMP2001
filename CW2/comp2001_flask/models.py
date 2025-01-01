import pytz
from config import db, ma
from marshmallow import fields

class TrailFeature(db.Model):
    __tablename__ = "TrailFeatures"
    __table_args__ = {'schema': 'CW2'}

    TrailId = db.Column(db.Integer, db.ForeignKey("CW2.Trail.TrailId"), primary_key=True)
    FeaturesId = db.Column(db.Integer, db.ForeignKey("CW2.Features.FeaturesId"), primary_key=True)

class TrailFeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TrailFeature
        load_instance = True
        sqla_session = db.session
        include_fk = True

trailFeature_schema = TrailFeatureSchema()

class Features(db.Model):
    __tablename__ = "Features"
    __table_args__ = {'schema': 'CW2'}

    FeaturesId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Feature = db.Column(db.String(20), nullable=False)

    trail_features = db.relationship(
        "TrailFeature",
        backref="feature",
        cascade="all, delete, delete-orphan",
        single_parent=True,
    )

class FeaturesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Features
        load_instance = True
        sqla_session = db.session
        include_relationships = True

feature_schema = FeaturesSchema()
features_schema = FeaturesSchema(many=True)

class Trail(db.Model):
    __tablename__ = "Trail"
    __table_args__ = {'schema': 'CW2'}

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

    trail_features = db.relationship(
        "TrailFeature",
        backref="trail",
        cascade="all, delete, delete-orphan",
        single_parent=True,
    )

class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        load_instance = True
        sqla_session = db.session
        include_relationships = True

    trail_features = fields.Nested(TrailFeatureSchema, many=True)

trail_schema = TrailSchema()
trails_schema = TrailSchema(many=True)
