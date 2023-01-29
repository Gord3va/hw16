from flask import Blueprint, jsonify, request
from app.bp.functions import Functions
from db.models.models import Order
from app.bp.api import bp

func = Functions()


@bp.get('/')
def get_all_orders():
    # Вывод всех "заказов"
    return jsonify(func.get_all(Order))


@bp.get('/<int:id>')
def get_order_by_id(id):
    # Вывод одного "заказа" по его id
    return jsonify(func.get_by_id(Order, id))


@bp.post('/')
def create_order():
    # Добавление "заказа" в таблицу orders
    func.insert_data_order([request.json])
    return jsonify(request.json)


@bp.put('/<int:id>')
def update_order(id):
    # Обновление "заказа" в таблице orders
    func.update_data(Order, id, request.json)
    return jsonify(request.json)


@bp.delete('/<int:id>')
def delete_order(id):
    # Удаление "заказа" из таблицы orders
    result = func.delete_data(Order, id)
    return jsonify(result)
