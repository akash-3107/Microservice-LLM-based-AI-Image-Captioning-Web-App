from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class CaptionLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_name = db.Column(db.String(120))
    image_path = db.Column(db.String(120))
    caption = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
