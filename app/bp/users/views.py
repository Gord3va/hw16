from flask import jsonify, request
from app.bp.functions import Functions, get_data_for_table, create_table
from app.configs.path import ORDERS_JSON_DIR
from db.models.models import User
from app.bp.api import users_bp


@users_bp.before_app_first_request
def first_request():
    users_data = get_data_for_table(ORDERS_JSON_DIR)
    create_table(users_data, User)


@users_bp.get('/')
def get_all_users():
    # Вывод всех "пользователей"
    # return jsonify(func.get_all(User))
    users = [user.t_dict() for user in User.query.all()]
    return jsonify(users)

@users_bp.get('/<int:uid>')
def get_user_by_id(uid):
    # Вывод одного "пользователя" по его id
    # return jsonify(func.get_by_id(User, uid))
    user = User.query.filter(User.id == uid).first()
    return jsonify(user.t_dict())


@users_bp.post('/')
def create_user():
    # Добавление "пользователя" в таблицу users
    # func.insert_data_user([request.json])
    # return jsonify(request.json)
    user = request.get_json()
    new_user = Functions(User).add_object(user)
    return jsonify(new_user)

@users_bp.put('/<int:uid>')
def update_user(uid):
    # # Обновление "пользователя" в таблице users
    # func.update_data(User, uid, request.json)
    # return jsonify(request.json)
    user = request.get_json()
    new_user = Functions(User).update_object(user, uid)
    return jsonify(new_user)


@users_bp.delete('/<int:uid>')
def delete_user(uid):
    # # Удаление "пользователя" из таблицы users
    # result = func.delete_data(User, uid)
    # return jsonify(result)
    deleted_user = Functions(User).delete_object(uid)
    return jsonify(deleted_user)
