from dbimport import db as base
from dbimport import ma

class Appearance(base.Model):
    __tablename__ = 'appearances'
    id = base.Column(base.Integer, primary_key=True)
    rating = base.Column(base.Integer, nullable=False)
    episode_id = base.Column(base.Integer, base.ForeignKey('episodes.id'), nullable=False)
    guest_id = base.Column(base.Integer, base.ForeignKey('guests.id'), nullable=False)

    episode = base.relationship('Episode', back_populates='appearances')
    guest = base.relationship('Guest', back_populates='appearances')

class AppearanceSchema(ma.Schema):
    class Meta:
        model = Appearance
        fields = ('id', 'rating', 'episode_id', 'guest_id', 'guest', 'episode')

    guest = ma.Nested('GuestSchema', exclude=('appearances',))
    episode = ma.Nested('EpisodeSchema', exclude=('appearances',))

appearance_schema = AppearanceSchema()
appearances_schema = AppearanceSchema(many=True)