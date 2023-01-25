from flask import Blueprint, jsonify, request
from functions import Functions
from models import Offer

bp_offers = Blueprint('bp_offers', __name__)
func = Functions()


@bp_offers.get('/')
def get_all_offers():
    # Вывод всех "предложений"
    return jsonify(func.get_all(Offer))


@bp_offers.get('/<int:id>')
def get_offer_by_id(id):
    # Вывод одного "предложения" по его id
    return jsonify(func.get_by_id(Offer, id))


@bp_offers.post('/')
def create_offer():
    # Добавление "предложения" в таблицу offers
    func.insert_data_offer([request.json])
    return jsonify(request.json)


@bp_offers.put('/<int:id>')
def update_offer(id):
    # Обновление "предложения" в таблице offers
    func.update_data(Offer, id, request.json)
    return jsonify(request.json)


@bp_offers.delete('/<int:id>')
def delete_offer(id):
    # Удаление предложения из таблицы offers
    result = func.delete_data(Offer, id)
    return jsonify(result)
