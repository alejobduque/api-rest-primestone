from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TableJSON(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # json_column = db.Column(JSON)
    name = db.Column(db.String(80))
    height = db.Column(db.String(20))
