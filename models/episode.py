from dbimport import db, ma

class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    

class EpisodeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Episode
        include_relationships = True
        load_instance = True
        fields = ('id', 'title', 'description', 'appearances')

episode_schema = EpisodeSchema()
episodes_schema = EpisodeSchema(many=True)