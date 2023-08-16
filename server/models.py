from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Project(db.Model, SerializerMixin):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    style = db.Column(db.String)
    size = db.Column(db.Float)
    color = db.Column(db.String)
    inventory = db.Column(db.Integer)

    def __repr__(self):
        return f"<Brand {self.brand} | Style {self.style} | Color {self.color} | Size {self.size} | Inventory {self.inventory}>"
