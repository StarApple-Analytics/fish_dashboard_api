from api import db

class Fish(db.Model):

    __tablename__ = "fishes"

    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    length = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    width = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Fish(id:{self.id}, species:{self.species}, length:{self.length}, height:{self.height}, width:{self.width})"
