from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def create_table(app):

    with app.app_context():
        db.create_all()

def main():
    create_table()

if __name__ == "__main__":
    main()