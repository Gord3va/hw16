import json
from config import db
from models import User, Order, Offer


class Functions:

    def get_all(self, model) -> list[dict]:
        """получить всех"""
        query = model.query.all()
        result = []
        for i in query:
            result.append(i)
        return result


