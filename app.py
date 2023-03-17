"""Flask app for adopt app."""

import os

from flask import Flask, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, UpdatePetForm

from models import connect_db, Pet, db

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
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get('/')
def show_homepage():
    """Displays homepage and list of current pets at our adoption agency."""
    pets = Pet.query.all()
    print(type(pets[0].available), 'Is this updating?')

    return render_template('homepage.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Get Route: Displays the add pet form. 
       Post Route: Allows the user to add a new pet to the homepage. Adds the new pet
       to the database and redirects the user to the list of pets."""

    form = AddPetForm()

    if form.validate_on_submit():

        # grab updated data from form
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        # update pet info
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()

        flash(f"Added {name} to our list of available pets! Let's find them a home!")
        return redirect('/')

    else:
        return render_template('add_pet_form.html', form=form)

@app.route('/<int:id>', methods=['GET', 'POST'])
def show_and_edit_pet_profile(id):
    """Get Route: Shows pet's profile.
       Post Route: Allows the user to update the pet's information. Commits that information
       to the database and redirects the user to the pet's profile."""
    
    pet = Pet.query.get(id)
    form = UpdatePetForm(obj=pet)
   
    if form.validate_on_submit():

        # grab updated data from form
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        # update pet info
        pet.photo_url = photo_url
        pet.notes = notes
        pet.available = available
        db.session.commit()

        return redirect(f'/{id}')

    else:
        return render_template('pet_profile.html', pet=pet, form=form)


