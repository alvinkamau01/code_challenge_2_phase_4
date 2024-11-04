# app.py
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from flask_migrate import Migrate
from dbimport import db, ma
from models.appearance import Appearance, appearance_schema, appearances_schema
from models.episode import Episode,episode_schema,episodes_schema
from models.guest import Guest,guests_schema,guest_schema
from seed import seed_episodes, seed_guests, seed_appearances
import os

# Create Flask app
app = Flask(__name__ ,template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///show.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)
print("Template folder path:", os.path.abspath(os.path.join(app.root_path, 'templates')))

@app.route('/episodes', methods=['GET'])
def get_episodes():
    """Retrieve all episodes."""
    episodes = Episode.query.all()
    results = episodes_schema.dump(episodes)
    return jsonify(results)

@app.route('/episodes/<int:episode_id>', methods=['GET'])
def get_episode(episode_id):
    """Retrieve a specific episode by ID."""
    episode = Episode.query.get(episode_id)
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404
    result = episode_schema.dump(episode)
    return jsonify(result)

@app.route('/guests', methods=['GET'])
def get_guests():
    """Retrieve all guests."""
    guests = Guest.query.all()
    results = guests_schema.dump(guests)
    return jsonify(results)

@app.route('/add_appearance')
def add_appearance_form():
    return render_template('add_appearance.html')

@app.route('/appearances', methods=['POST'])
def add_appearance():
    """Add a new appearance."""
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

def create_tables():
    """Create database tables."""
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    with app.app_context():
        seed_episodes()
        seed_guests()
        seed_appearances()
    app.run(debug=True)