"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField('Pet Name',
                       validators=[InputRequired(message='Please enter valid name.')])
    species = StringField('Species',
                          validators=[AnyOf(['cat', 'dog', 'porcupine'], message='Only accepting cats, dogs, and porcupines.')])
    photo_url = StringField('Photo URL',
                            validators=[Optional(),
                                        URL(message='Please enter valid URL.')])
    age = SelectField('Age', choices=[('baby', 'Baby'),
                                      ('young', 'Young'),
                                      ('adult', 'Adult'),
                                      ('senior', 'Senior')])
    notes = StringField('What do prospective adopters need to know about your pet?')


class UpdatePetForm(FlaskForm):
    """Form for updating pet information."""

    # NOTE: why coerce boolean to boolean?
    available = BooleanField('Is available?')
    photo_url = StringField('Photo URL',
                            validators=[Optional(), URL(message='Please enter valid URL.')])
    notes = StringField('What do prospective adopters need to know about your pet?')