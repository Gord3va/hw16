from flask import Blueprint, jsonify, request
from functions import Functions
from models import User

bp_users = Blueprint('blueprint_users', __name__)
func = Functions()


@bp_users.get('/')
def get_all_users():
    # Вывод всех "пользователей"
    return jsonify(func.get_all(User))


@bp_users.get('/<int:id>')
def get_user_by_id(id):
    # Вывод одного "пользователя" по его id
    return jsonify(func.get_by_id(User, id))


@bp_users.post('/')
def create_user():
    # Добавление "пользователя" в таблицу users
    func.insert_data_user([request.json])
    return jsonify(request.json)


@bp_users.put('/<int:id>')
def update_user(id):
    # Обновление "пользователя" в таблице users
    func.update_data(User, id, request.json)
    return jsonify(request.json)


@bp_users.delete('/<int:id>')
def delete_user(id):
    # Удаление "пользователя" из таблицы users
    result = func.delete_data(User, id)
    return jsonify(result)
