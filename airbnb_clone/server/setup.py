from app import db
from models import Property

db.create_all()

# Add some sample data
properties = [
    Property(
        name="Velhe, Torna-Rajgad, India",
        location="Mountain and pool views",
        date_range="21–26 Jul",
        price="₹10,540",
        rating=4.9,
        image_url="images/living1.webp",
    ),
    Property(
        name="Gokarna, India",
        location="Mountain and pool views",
        date_range="18–23 Jun",
        price="₹39,184",
        rating=4.9,
        image_url="images/living2.webp",
    ),
    Property(
        name="Lonavla, India",
        location="Mountain and pool views",
        date_range="4–9 Jul",
        price="₹34,234",
        rating=5.0,
        image_url="images/living3.webp",
    ),
    Property(
        name="Udaipur, India",
        location="Mountain and pool views",
        date_range="18–23 Jun",
        price="₹23,280",
        rating=5.0,
        image_url="images/living4.webp",
    ),
    Property(
        name="Vathalmalai, India",
        location="Mountain and pool views",
        date_range="19–24 Jun",
        price="₹24,737",
        rating=5.0,
        image_url="images/amazing1.jpg",
    ),
]

for prop in properties:
    db.session.add(prop)

db.session.commit()