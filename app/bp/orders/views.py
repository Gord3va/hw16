from flask import jsonify, request
from app.bp.functions import Functions, get_data_for_table, create_table
from app.configs.path import ORDERS_JSON_DIR
from db.models.models import Order
from app.bp.api import orders_bp


@orders_bp.before_app_first_request
def first_request():
    orders_data = get_data_for_table(ORDERS_JSON_DIR)
    create_table(orders_data, Order)


@orders_bp.get('/')
def get_all_orders():
    # Вывод всех "заказов"
    # return jsonify(func.get_all(Order))
    orders = [order.t_dict() for order in Order.query.all()]
    return jsonify(orders)


@orders_bp.get('/<int:uid>')
def get_order_by_id(uid):
    # Вывод одного "заказа" по его id
    # return jsonify(func.get_by_id(Order, uid))
    order = Order.query.filter(Order.id == uid).first()
    return jsonify(order.t_dict())


@orders_bp.post('/')
def create_order():
    # Добавление "заказа" в таблицу orders
    # func.insert_data_order([request.json])
    # return jsonify(request.json)
    order = request.get_json()
    new_order = Functions(Order).add_object(order)
    return jsonify(new_order)


@orders_bp.put('/<int:uid>')
def update_order(uid):
    # Обновление "заказа" в таблице orders
    # func.update_data(Order, uid, request.json)
    # return jsonify(request.json)
    order = request.get_json()
    new_order = Functions(Order).update_object(order, uid)
    return jsonify(new_order)


@orders_bp.delete('/<int:uid>')
def delete_order(uid):
    # Удаление "заказа" из таблицы orders
    # result = func.delete_data(Order, uid)
    # return jsonify(result)
    deleted_order = Functions(Order).delete_object(uid)
    return jsonify(deleted_order)
