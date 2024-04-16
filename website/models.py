from . import db
from flask_login import UserMixin
from sqlalchemy import func

class News(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  data = db.Column(db.String(10000))
  date = db.Column(db.DateTime(timezone = True), default = func.now())
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key = True)
  email = db.Column(db.String(115), unique= True)
  password = db.Column(db.String(115))
  first_name = db.Column(db.String(115))
  last_name = db.Column(db.String(115))
  post = db.relationship('News')



