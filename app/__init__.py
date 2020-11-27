from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

# Instantiate Flask extensions
db = SQLAlchemy()
migrate = Migrate()


# Initialize Flask Application
def create_app():
    """Create a Flask application.
        """
    # Instantiate Flask
    app = Flask(__name__)
    # # Load settings
    app.config.from_object(Config)

    # Setup Flask-SQLAlchemy
    db.init_app(app)

    # Setup Flask-Migrate
    migrate.init_app(app, db)

    import app.talk.controllers as pets
    app.register_blueprint(pets.module)
    return app