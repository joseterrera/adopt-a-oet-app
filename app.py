"""Flask app for adopt a pet"""
from flask import Flask, url_for, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] ='cookie'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"

app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

connect_db(app)
db.create_all()

# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.route('/')
def list_pets():
  """list all pets"""

  pets = Pet.query.all()
  return render_template('pet_list.html', pets=pets)


# @app.route("/add", methods=["GET", "POST"])
# def add_pet():
#   """Add a pet."""

#   form = AddPetForm()

#   if form.validate_on_submit():
#       data = {k: v for k, v in form.data.items() if k != "csrf_token"}
#       new_pet = Pet(**data)
#       # new_pet = Pet(name=form.name.data, age=form.age.data, ...)
#       db.session.add(new_pet)
#       db.session.commit()
#       flash(f"{new_pet.name} added.")
#       return redirect(url_for('list_pets'))

#   else:
#       # re-present form for editing
#       return render_template("pet_add_form.html", form=form)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
  """Add a pet."""
  
  form = AddPetForm()

  if form.validate_on_submit():
    # below is a dictionary (key: value) comprehension, which is a method for 
    # transforming one dictionary into another dictionary.
    # We will create new key/value pairs with the submitted new form data and
    # add it to the new dictionary
    # We will also exclude all hidden values
    data = {k: v for k, v in form.data.items() if k != 'csrf token'}
    # (**data) unpack the dictionary values so they are sent as separate keyword arguments. One asterisk for a list, two asterisks for a dictionary.
    new_pet = Pet(**data)
    db.session.add(new_pet)
    db.session.commit()
    flash(f"{new_pet_name} added.")
    return redirect(url_for('list_pets'))

  else: 
    return render_template('pet_add_form.html', form=form)

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
  """Edit pet."""
  pet = Pet.query.get_or_404(pet_id)
  form = EditPetForm(obj=pet)

  if form.validate_on_submit():
    pet.notes = form.notes.data
    pet.available = form.available.data
    pet.photo.url = form.photo_url.data
    db.session.commit()
    flash(f"{pet.name} updated.")
    return redirect(url_for('list_pets'))

  else:
    # failed, re-present form for editing
    return render_template('pet_edit_form.html', form=form, pet=pet)
      

@app.route('/api/pets/<int:pet_id>', methods=["GET"])
def api_get_pet(pet_id):
  """Return basic info about pet in JSON"""

  pet = Pet.query.get_or_404(pet_id)
  info = {"name": pet.name, "age": pet.age}

  return jsonify(info)





