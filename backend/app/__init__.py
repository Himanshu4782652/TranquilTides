from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os
# from .routes import main

db = SQLAlchemy()


def create_app(config_name=None):
    # Create Flask app instance
    app = Flask(__name__)

    # Determine which config to use based on the environment
    if config_name is None:
        config_name = os.getenv("FLASK_ENV", "development")

    # Load config from the config file dynamically
    app.config.from_object(f"backend.config.{config_name.capitalize()}Config")

    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)

    # Initialize LoginManager
    login_manager = LoginManager()
    login_manager.login_view = "main.login"  # Set the default login view
    login_manager.init_app(app)

    # User loader callback for Flask-Login
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(
            int(user_id)
        )  # Flask-Login requires this to load users by ID

    # Register blueprints
    from .routes import main

    app.register_blueprint(main)

    return app
