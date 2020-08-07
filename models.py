"""Models for adopt a pet"""

from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMAGE = 'https://picsum.photos/id/237/200/300';

db = SQLAlchemy()


class Pet(db.Model):
  """Pet to adopt"""
  __tablename__ = 'pets'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, nullable=False)
  species = db.Column(db.Text, nullable=False)
  photo_url = db.Column(db.Text)
  age = db.Column(db.Integer)
  notes = db.Column(db.Text)
  available = db.Column(db.Boolean, nullable=False, default=True)

  def image_url(self):
    """Return image for pet"""
    return self.photo_url or DEFAULT_IMAGE


def connect_db(app):
    """Connect this database to provided Flask app. 
       You should call this in your Flask app."""

    db.app = app
    db.init_app(app)

    