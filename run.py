import os

from app import create_app
from config import DevConfig
from db import db
from models import User


app = create_app(config=DevConfig)

@app.shell_context_processor
def shell():
    return {
        "db":db,
        "User":User,
    }