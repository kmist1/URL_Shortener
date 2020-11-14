from .db import db

class User(db.Document):
    firstName = db.StringField(required=True)
    LastName = db.StringField(required=True)
    Email = db.StringField(required=True, unique=True)
