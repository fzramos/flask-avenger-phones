from flask import Flask

# adding config object
from config import Config

# Import the SQLAlchemy object
from flask_sqlalchemy import SQLAlchemy

# Import the Migrate object
from flask_migrate import Migrate

app = Flask(__name__)
# complete config cycle for our flask app
# and give access to our Database(when we have one)
# along with our Secret key
app.config.from_object(Config)

# Init our database (db)
db = SQLAlchemy(app)

# Init the migrator
migrate = Migrate(app, db)

from avengers_app import routes, models
