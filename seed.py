"""Seed file to make sample data for users db."""

from models import db, connect_db, Pet
from app import app
from flask_sqlalchemy import SQLAlchemy

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
# An alternative if you don't want to drop
# and recreate your tables:
# User.query.delete()

rocky = Pet(name='Rocky', species='Dog', photo_url='https://dehayf5mhw1h7.cloudfront.net/wp-content/uploads/sites/427/2018/05/22060509/dog-puppy-200x200.jpg', age='baby', notes='Likes to play fetch!', available=False)
sandy = Pet(name='Sandy', species='Cat', photo_url='https://www.hillspet.co.nz/content/dam/cp-sites/hills/hills-pet/en_us/exported/cat-care/healthcare/images/seniorCatBrainAging.jpg', age='adult', notes='Mean!', available=True)
porky = Pet(name='Porky', species='Porcupine', photo_url='', age='senior', notes='Prickly', available=True)

db.session.add(rocky)
db.session.add(sandy)
db.session.add(porky)

db.session.commit()