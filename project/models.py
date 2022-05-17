from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, validates

db = SQLAlchemy()


class Contacts(db.Model):
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<id {self.id}>"
