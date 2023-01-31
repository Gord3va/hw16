from flask import jsonify, request
from app.bp.functions import get_data_for_table, create_table, Functions
from app.configs.path import OFFERS_JSON_DIR
from db.models.models import Offer
from app.bp.api import offers_bp


@offers_bp.before_app_first_request
def first_request():
    offers_data = get_data_for_table(OFFERS_JSON_DIR)
    create_table(offers_data, Offer)


@offers_bp.get('/')
def get_all_offers():
    # Вывод всех "предложений"
    # return jsonify(func.get_all(Offer))
    offers = [offer.t_dict() for offer in Offer.query.all()]
    return jsonify(offers)


@offers_bp.get('/<int:uid>')
def get_offer_by_id(uid):
    # Вывод одного "предложения" по его id
    # return jsonify(func.get_by_id(Offer, uid))
    offer = Offer.query.filter(Offer.id == uid).first()
    return jsonify(offer.t_dict())


@offers_bp.post('/')
def create_offer():
    # Добавление "предложения" в таблицу offers
    # func.insert_data_offer([request.json])
    # return jsonify(request.json)
    offer = request.get_json()
    new_offer = Functions(Offer).add_object(offer)
    return jsonify(new_offer)


@offers_bp.put('/<int:uid>')
def update_offer(uid):
    # Обновление "предложения" в таблице offers
    # func.update_data(Offer, uid, request.json)
    # return jsonify(request.json)
    offer = request.get_json()
    new_offer = Functions(Offer).update_object(offer, uid)
    return jsonify(new_offer)


@offers_bp.delete('/<int:uid>')
def delete_offer(uid):
    # Удаление предложения из таблицы offers
    # result = func.delete_data(Offer, uid)
    # return jsonify(result)
    deleted_offer = Functions(Offer).delete_object(uid)
    return jsonify(deleted_offer)
