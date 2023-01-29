import db
from db.models.models import User, Order, Offer

import json
from db import db


class Functions:

    def insert_data_user(self, input_data: list):
        """Запись данных в таблицу users"""
        for user in input_data:
            db.session.add(User(
                id=user.get('id'),
                first_name=user.get('first_name'),
                last_name=user.get('last_name'),
                age=user.get('age'),
                email=user.get('email'),
                role=user.get('role'),
                phone=user.get('phone'),
            ))
        db.session.commit()

    def insert_data_order(self, input_data: list):
        """Запись данных в таблицу orders"""
        for order in input_data:
            db.session.add(Order(
                id=order.get('id'),
                name=order.get('name'),
                description=order.get('description'),
                start_date=order.get('start_date'),
                end_date=order.get('end_date'),
                address=order.get('address'),
                price=order.get('price'),
                customer_id=order.get('customer_id'),
                executor_id=order.get('executor_id'),
            ))
        db.session.commit()

    def insert_data_offer(self, input_data: list):
        """Запись данных в таблицу offers"""
        for offer in input_data:
            db.session.add(Offer(
                id=offer.get('id'),
                order_id=offer.get('order_id'),
                executor_id=offer.get('executor_id'),
            ))
        db.session.commit()

    def init_base(self):
        """Удаляем таблицы, создаем таблицы и загружаем данные из json файлов из папки data"""
        db.drop_all()
        db.create_all()
        with open('data/users.json', "r", encoding="utf-8") as file:
            self.insert_data_user(json.load(file))

        with open('data/orders.json', "r", encoding="utf-8") as file:
            self.insert_data_order(json.load(file))

        with open('data/offers.json', "r", encoding="utf-8") as file:
            self.insert_data_offer(json.load(file))

        db.session.commit()

    def get_all(self, model) -> list[dict]:
        """Получение всех объектов таблиц"""
        query = model.query.all()
        result = []
        for item in query:
            result.append(item.to_dict())
        return result

    def get_by_id(self, model, id: int) -> dict:
        """Получение объекта таблицы по его id"""
        try:
            result = model.query.get(id).to_dict()
            return result
        except Exception:
            return "Данные отсутствуют"

    def update_data(self, model, id: int, input_data):
        """Обновление объекта таблицы по его id"""
        try:
            db.session.query(model).filter(model.id == id).update(input_data)
            db.session.commit()
        except Exception:
            return "Ошибка обновления данных"

    def delete_data(self, model, id: int):
        """Удаление объекта таблицы по его id"""
        try:
            query = db.session.query(model).get(id)
            db.session.delete(query)
            db.session.commit()
            return "Данные удалены"
        except Exception:
            return "Данные отсутствуют"
