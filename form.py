from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email

class AddPet(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet name")
    species = StringField('Species')
    photo_url = StringField('Photo URL')
    age = SelectField("Age", choices=[(1,1),(2,2),(3,3),(4,4)])
    notes = StringField('Notes')
    is_available = BooleanField('Is Available')
