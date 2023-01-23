from config import db

"""
ПРИМЕР
{'id': 1, 
'first_name': 'Hudson', 
'last_name': 'Pauloh',
 'age': 31, 
 'email': 'elliot16@mymail.com',
  'role': 'customer', 
  'phone': '6197021684'}
  """

"""пользователь, его данные"""


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)  # id уникальный ключ
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.Text)
    role = db.Column(db.Text)
    phone = db.Column(db.Integer)


"""
ПРИМЕР
{'id': 0, 
'name': 'Встретить тетю на вокзале', 
'description': 'Встретить тетю на вокзале с табличкой. Отвезти ее в магазин, помочь погрузить покупки.
 Привезти тетю домой, занести покупки и чемодан в квартиру', 
 'start_date': '02/08/2013', 
 'end_date': '03/28/2057', 
 'address': '4759 William Haven Apt. 194\nWest Corey, TX 43780', 
 'price': 5512, 
 'customer_id': 3, 
 'executor_id': 6}
"""

"""заказ, данные о заказе"""


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    address = db.Column(db.Text)
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('offers.id'))


"""
ПРИМЕР
{'id': 0,
 'order_id': 36, 
 'executor_id': 10}, 
"""

"""заказчик и заказ, исполнитель связь"""

class Offer(db.Model):
    __tablename__ = 'offers'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.db'))
    executor_id = db.Column(db.Integer, db.ForeignKey('users.db'))

