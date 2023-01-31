from flask import Blueprint

offers_bp = Blueprint('offers', __name__, url_prefix='/offers')
orders_bp = Blueprint('orders', __name__, url_prefix='/orders')
users_bp = Blueprint('users', __name__, url_prefix='/users')
