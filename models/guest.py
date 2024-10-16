from dbimport import db as base
from dbimport import ma

class Guest(base.Model):
    __tablename__ = 'guests'  # Changed to plural for convention
    id = base.Column(base.Integer, primary_key=True)
    name = base.Column(base.String(100), nullable=False)
    bio = base.Column(base.String(200), nullable=False)  # Changed 'column' to 'bio' for clarity
    
    appearances = base.relationship('Appearance', back_populates='guest', cascade='all, delete-orphan')

class GuestSchema(ma.Schema):
    class Meta:
        model = Guest
        fields = ('id', 'name', 'bio', 'appearances')
    
    appearances = ma.List(ma.Nested('AppearanceSchema', exclude=('guest',)))

guest_schema = GuestSchema()
guests_schema = GuestSchema(many=True)