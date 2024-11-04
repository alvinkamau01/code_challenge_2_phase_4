from dbimport import db, ma

class Guest(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.String(200), nullable=False)

  
class GuestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Guest
        include_relationships = True
        load_instance = True
        fields = ('id', 'name', 'bio', 'appearances')

guest_schema = GuestSchema()
guests_schema = GuestSchema(many=True)