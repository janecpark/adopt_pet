from flask import Flask, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from form import AddPet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    """Display homepage"""
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

@app.route('/add', methods=["POST"])
def add_pet():
    """Form for adding pets"""
    form = AddPet()

    if form.validate_on_submit():

        name = form.name.data 
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        is_available= form.is_available.data 

        pet = Pet(name=name, species=species,photo_url=photo_url, age=age, notes=notes, is_available=is_available)
        db.session.add(pet)
        db.session.commit()

        flash(f"Added {pet.name}")
        return redirect('/')
    else:
        return render_template('form.html', form=form)

