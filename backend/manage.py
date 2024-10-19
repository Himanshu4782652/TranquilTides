from app import create_app, db
from flask_migrate import Migrate
from flask.cli import with_appcontext
import click

app = create_app()

# Initialize Flask-Migrate
migrate = Migrate(app, db)


# Custom commands using Flask CLI
@click.command(name="create_db")
@with_appcontext
def create_db():
    """Create the database (sqlite)"""
    db.create_all()


@click.command(name="drop_db")
@with_appcontext
def drop_db():
    """Drop the database"""
    db.drop_all()


if __name__ == "__main__":
    app.cli.add_command(create_db)
    app.cli.add_command(drop_db)
    app.run()
