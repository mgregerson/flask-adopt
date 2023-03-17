"""Flask app for adopt app."""

import os

from flask import Flask, redirect, render_template, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm

from models import connect_db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get('/')
def show_homepage():
    pets = Pet.query.all()
    print(type(pets[0].available), 'Is this updating?')

    return render_template('homepage.html', pets=pets)

@app.route('/add', methods=['GET', 'POST']):
def add_pet():
    """Pet add form; handle adding pet."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        flash(f"Added {name} to our list of available pets! Let's find them a home!")
        return redirect('/')
    
    else:
        return render_template('add_pet_form.html', form=form)
