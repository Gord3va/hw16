import os

from flask import Flask

from app.bp.api import bp
from app.configs.config import DevConfig, ProdConfig
from db.db import db

app = Flask(__name__)

app.register_blueprint(bp)

if os.getenv('FLASK_ENV') == 'development':
    app.config.from_object(DevConfig)
else:
    app.config.from_object(ProdConfig)

db.init_app(app)
