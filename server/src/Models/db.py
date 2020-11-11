from flask_mongoengine import MongoEngine

# Intializing database
db = MongoEngine()

def intialize_db(app):
    db.init_app(app)