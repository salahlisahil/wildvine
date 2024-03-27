from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subtitle = db.Column(db.String(200))
    title = db.Column(db.String(200))
    text = db.Column(db.Text)
    description = db.Column(db.String)
    date = db.Column(db.DateTime, default=datetime.utcnow)


class Views(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subtitle = db.Column(db.String(200))
    title = db.Column(db.String(200))
    text = db.Column(db.Text)
    name = db.Column(db.Text)
    lower_title = db.Column(db.Text)

    def __repr__(self):
        return f"Event('{self.title}', '{self.subtitle}', {self.description})"
