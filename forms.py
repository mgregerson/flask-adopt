"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField('Pet Name')
    species = StringField('Species')
    photo_url = StringField('Photo URL')
    age = SelectField('Age', choices=[('baby', 'Baby'), 
                                      ('young', 'Young'), 
                                      ('adult', 'Adult'), 
                                      ('senior', 'Senior')])
    notes = StringField('What do prospective adopters need to know about your pet?')




# Create a form for adding pets. This should use Flask-WTF, and should have the following fields:

# Pet name
# Species
# Photo URL
# Age
# Notes
# This should be at the URL path /add. Add a link to this from the homepage.