from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DEV_DATA_BASE_DIR = BASE_DIR.joinpath('db', 'development.db')
JSON_DIR = BASE_DIR.joinpath('db', 'jsons_files')
USER_JSON_DIR = JSON_DIR.joinpath('users.json')
OFFERS_JSON_DIR = JSON_DIR.joinpath('offers.json')
ORDERS_JSON_DIR = JSON_DIR.joinpath('orders.json')
