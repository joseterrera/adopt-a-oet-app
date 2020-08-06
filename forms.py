from flask_wtf import FlaskForm
from wtForms import StrinField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
  """Form for adding pets."""

  name = StringField(
    "Pet Name", validators=[InputRequired()] )
  
  species = SelectField(
    "Species",
    choices=[('cat', 'Cat'), ('dog', 'Dog'), ('pig', 'pig') ] )
  
  photo_url = StringField(
    'Photo URL', validates=[Optional(), URL()] )
  
  age = IntegerField(
    'Age', validators=[Optional(), NumberRange(min=0, nax=30)] )

  notes = TextAreafield("Comments", validators=[Optional(), length(min=10)] )

class EditPetForm(FlaskForm):
  """Form for editing an existing pet."""

  photo_url = StringField("Photo URL", validators=[Optional(), URL()])

  notes = TextAreaField(
    "Comments", validators[Optional(), Length(min=10)]
  )

  available = BooleanField('Available')