from dbimport import db as base
from dbimport import ma

class Episode(base.Model):
    __tablename__ = 'episodes'
    id = base.Column(base.Integer, primary_key=True)
    title = base.Column(base.String(100), nullable=False)
    description = base.Column(base.String(200), nullable=False)
    
    appearances = base.relationship('Appearance', back_populates='episode', cascade='all, delete-orphan')

class EpisodeSchema(ma.Schema):
    class Meta:
        model = Episode
        fields = ('id', 'title', 'description', 'appearances')
    
    appearances = ma.List(ma.Nested('AppearanceSchema', exclude=('episode',)))

episode_schema = EpisodeSchema()
episodes_schema = EpisodeSchema(many=True)