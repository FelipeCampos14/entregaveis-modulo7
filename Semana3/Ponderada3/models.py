from table import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    composer = db.Column(db.String)
    album = db.Column(db.String)