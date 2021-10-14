import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import HackerWars

migrate = Migrate(app, db)

@app.route("/")
def index():
    return "Hello, world!"


@app.route('/<name>')
def hello_name(name):
    return "Hello, {}!".format(name)
