import os
from faker import Faker
from models.episode import Episode
from models.guest import Guest
from models.appearance import Appearance
from dbimport import db

fake = Faker()


def seed_episodes():
    for _ in range(10):
        episode = Episode(title=fake.text(max_nb_chars=50), description=fake.text(max_nb_chars=200))
        db.session.add(episode)
    db.session.commit()

def seed_guests():
    for _ in range(20):
        guest = Guest(name=fake.name(), bio=fake.text(max_nb_chars=200))
        db.session.add(guest)
    db.session.commit()

def seed_appearances():
    episodes = Episode.query.all()
    guests = Guest.query.all()
    for _ in range(50):
        episode = fake.random_element(episodes)
        guest = fake.random_element(guests)
        rating = fake.random_int(min=1, max=5)
        appearance = Appearance(episode_id=episode.id, guest_id=guest.id, rating=rating)
        db.session.add(appearance)
    db.session.commit()