from dbimport import db, ma

class Appearance(db.Model):
    __tablename__ = 'appearances'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)

    # Use string reference for the relationship
    episode = db.relationship("Episode", backref='appearances', lazy=True)
    guest = db.relationship("Guest", backref='appearances', lazy=True)

class AppearanceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Appearance
        include_relationships = True
        load_instance = True
        fields = ('id', 'rating', 'episode_id', 'guest_id', 'episode', 'guest')

appearance_schema = AppearanceSchema()
appearances_schema = AppearanceSchema(many=True)