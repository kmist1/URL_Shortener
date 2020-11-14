from .db import db

class Link(db.Document):
    long_link = db.StringField(required = True)
    sort_link = db.StringField(required=True)
    user_email = db.StringField(required = True)
