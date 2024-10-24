## Project Structure
├── app.py
├── dbimport.py
├── models
│   ├── __init__.py
│   ├── appearance.py
│   ├── episode.py
│   └── guest.py
├── seed.py
└── instance
    └── show.db

## Install required dependencies
pip install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy faker

## setup database
flask db init
flask db migrate
flask db upgrade

## Start development server
python app.py

## API Endpoints
GET /episodes: Retrieve all episodes
GET /episodes/<id>: Retrieve a specific episode
GET /guests: Retrieve all guests
POST /appearances: Add a new appearance

## Data Models
Episode: Represents a talk show episode
Guest: Represents a guest on the show
Appearance: Represents a guest's appearance on a specific episode

## Seeding data
The application includes a seeding script (seed.py) that populates the database with sample data using Faker. This script is automatically run when starting the application.

## Development
The project uses Flask-SQLAlchemy for database operations
Flask-Marshmallow is used for object serialization/deserialization
The database schema is defined in the model files under the models directory


## Running the app
To run the app, use python3 app.py then onto the url at the top add the route to the data to be displayed. eg.  http://127.0.0.1:5000/episodes