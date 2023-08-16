from models import db, Project
from app import app


def seed_data():
    projects_data = [
        {
            "brand": "Brand A",
            "style": "Style 1",
            "size": 10.0,
            "color": "Red",
            "inventory": 50,
        },
        {
            "brand": "Brand B",
            "style": "Style 2",
            "size": 8.5,
            "color": "Blue",
            "inventory": 30,
        },
    ]

    for project in projects_data:
        new_project = Project(**project)
        db.session.add(new_project)

    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        seed_data()
