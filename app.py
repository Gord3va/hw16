import json
from typing import Type

import sqlalchemy.exc
from flask import Flask

from config import BaseConfig
from db import db
from models import User

def create_data():
    db.create.all()

    with open('fixtures/users.json', 'r', encoding='utf-8') as f:
        users = json.load(f)

        for user in users:
            db.session.app(User(**user))
        try:
            db.session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            print(f'Data already exsists: {e}')


def create_app(config: Type[BaseConfig]) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    app.before_first_request(create_data())

    @app.route('/')
    def index():
        return {'status': 'ok'}

    return app
