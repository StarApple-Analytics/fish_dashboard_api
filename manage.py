import os

from flask_migrate import Migrate
from flask.cli import FlaskGroup

from api import create_app, db


cli = FlaskGroup()
app = create_app()
migrate = Migrate(app, db)


if __name__ == '__main__':
	cli()