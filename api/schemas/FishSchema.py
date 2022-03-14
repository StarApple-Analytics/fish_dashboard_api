from api.extentions import ma
from api.models.Fish import Fish

class FishSchema(ma.SQLAlchemyAutoSchema):
    class Meta: 
        model = Fish
    
    id = ma.auto_field()
    species= ma.auto_field()
    weight = ma.auto_field()
    horizontal_length = ma.auto_field()
    vertical_length = ma.auto_field()
    diagonal_length = ma.auto_field()
    height = ma.auto_field()
    width = ma.auto_field()

