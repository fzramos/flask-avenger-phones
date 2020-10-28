from flask import Flask

# adding config object
from config import Config

app = Flask(__name__)
# complete config cycle for our flask app
# and give access to our Database(when we have one)
# along with our Secret key
app.config.from_object(Config)