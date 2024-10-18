from app import create_app, db
from flask_migrate import MigrateCommand
from flask_script import Manager

app = create_app()

manager = Manager(app)

# Add migration commands
from flask_migrate import Migrate

migrate = Migrate(app, db)


# Manager commands for running app and migrations
@manager.command
def run():
    app.run()


@manager.command
def create_db():
    """Create the database (sqlite)"""
    db.create_all()


@manager.command
def drop_db():
    """Drop the database"""
    db.drop_all()


@manager.command
def seed():
    """Seed the database with initial data (optional)"""
    pass  # Add seed logic if needed


if __name__ == "__main__":
    manager.run()
