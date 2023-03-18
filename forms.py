"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf


class AddPetForm(FlaskForm):
    """Form for adding pets."""
# TODO: Update formatting for properties in our form class.
    name = StringField(
        'Pet Name',
        validators=[
        InputRequired(message='Please enter valid name.')
        ]) 
    # Select field would work better for only allowing one of these three animals.
    species = StringField('Species',
                          validators=[AnyOf(['cat', 'dog', 'porcupine'], message='Only accepting cats, dogs, and porcupines.')])
    photo_url = StringField('Photo URL',
                            validators=[Optional(),
                                        URL(message='Please enter valid URL.')])
    age = SelectField('Age', choices=[('baby', 'Baby'),
                                      ('young', 'Young'),
                                      ('adult', 'Adult'),
                                      ('senior', 'Senior')])
    notes = StringField('What do prospective adopters need to know about your pet?', validators=[Optional()])


class UpdatePetForm(FlaskForm):
    """Form for updating pet information."""

    available = BooleanField('Is available?')
    photo_url = StringField('Photo URL',
                            validators=[Optional(), URL(message='Please enter valid URL.')])
    notes = StringField('What do prospective adopters need to know about your pet?', validators=[Optional()])