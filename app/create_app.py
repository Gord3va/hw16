import os

from flask import Flask

from app.bp.api import offers_bp
from app.bp.api import orders_bp
from app.bp.api import users_bp
from app.configs.config import DevConfig, ProdConfig
from db.create_db import db

app = Flask(__name__)

app.register_blueprint(offers_bp)
app.register_blueprint(orders_bp)
app.register_blueprint(users_bp)

if os.getenv('FLASK_ENV') == 'development':
    app.config.from_object(DevConfig)
else:
    app.config.from_object(ProdConfig)

db.init_app(app)
