from api.extentions import ma
from api.models.Fish import Fish

class FishSchema(ma.SQLAlchemyAutoSchema):
    class Meta: 
        model = Fish
    
    id = ma.auto_field()
    species= ma.auto_field()
    weight = ma.auto_field()
    length = ma.auto_field()
    height = ma.auto_field()
    width = ma.auto_field()

