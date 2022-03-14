from api import db

class Fish(db.Model):

    __tablename__ = "fishes"

    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String, nullable=True)
    weight = db.Column(db.Float, nullable=True)
    horizontal_length = db.Column(db.Float, nullable=True)
    vertical_length = db.Column(db.Float, nullable=True)
    diagonal_length = db.Column(db.Float, nullable=True)
    height = db.Column(db.Float, nullable=True)
    width = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f"Fish(id:{self.id}, species:{self.species}, length:{self.length}, height:{self.height}, width:{self.width})"
