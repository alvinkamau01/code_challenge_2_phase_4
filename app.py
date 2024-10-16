from flask import Flask, jsonify, request, abort
from flask_migrate import Migrate
from models import Appearance, Episode, Guest
from models import appearance_schema, appearances_schema, episode_schema, episodes_schema, guest_schema, guests_schema
from dbimport import db, ma, app

migrate = Migrate(app, db)

@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    results = episodes_schema.dump(episodes)
    return jsonify(results)

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404
    result = episode_schema.dump(episode)
    return jsonify(result)

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    results = guests_schema.dump(guests)
    return jsonify(results)

@app.route('/appearances', methods=['POST'])
def add_appearance():
    data = request.json
    episode_id = data.get('episode_id')
    guest_id = data.get('guest_id')
    rating = data.get('rating')

    if not all([episode_id, guest_id, rating]):
        return jsonify({'error': 'Missing required fields'}), 400

    episode = Episode.query.get(episode_id)
    guest = Guest.query.get(guest_id)

    if not episode or not guest:
        return jsonify({'error': 'Episode or Guest not found'}), 404

    new_appearance = Appearance(episode_id=episode_id, guest_id=guest_id, rating=rating)
    db.session.add(new_appearance)
    db.session.commit()

    return appearance_schema.jsonify(new_appearance), 201

from seed import seed_episodes, seed_guests, seed_appearances

def create_tables():
    db.create_all()

if __name__ == '__main__':
    with app.app_context():
        create_tables()
        seed_episodes()
        seed_guests()
        seed_appearances()
    app.run(debug=True)