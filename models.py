"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, request, flash

db = SQLAlchemy()

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet model"""

    __tablename__ = 'pets'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.Text,
        nullable=False
    )

    species = db.Column(
        db.Text,
        nullable=False
    )

    photo_url = db.Column(
        db.Text,
        nullable=False,
        default = ''

    )

    age = db.Column(
        db.Text,
        nullable=False,
    )

# TODO: Add a checkConstraint for age (db.CheckConstraint(age.in_(['baby', 'young', 'adult', 'senior'])))
    
    notes = db.Column(
        db.Text,
        nullable=True
    )

    available = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )


   