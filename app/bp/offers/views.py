from flask import Blueprint, jsonify, request
from app.bp.functions import Functions
from db.models.models import Offer
from app.bp.api import bp

func = Functions()


@bp.get('/')
def get_all_offers():
    # Вывод всех "предложений"
    return jsonify(func.get_all(Offer))


@bp.get('/<int:id>')
def get_offer_by_id(id):
    # Вывод одного "предложения" по его id
    return jsonify(func.get_by_id(Offer, id))


@bp.post('/')
def create_offer():
    # Добавление "предложения" в таблицу offers
    func.insert_data_offer([request.json])
    return jsonify(request.json)


@bp.put('/<int:id>')
def update_offer(id):
    # Обновление "предложения" в таблице offers
    func.update_data(Offer, id, request.json)
    return jsonify(request.json)


@bp.delete('/<int:id>')
def delete_offer(id):
    # Удаление предложения из таблицы offers
    result = func.delete_data(Offer, id)
    return jsonify(result)
