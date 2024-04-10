from . import db
from flask_login import UserMixin

class user(db.model):
  id = db.column(db.Integer, primary_key = True)
  email = db.column(db.String(115), unique= True)
  password =  db.column(db.String(115))
  first_name = db.column(db.String(115))
  last_name =  db.column(db.String(115))



