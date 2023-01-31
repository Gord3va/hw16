from db.create_db import db
import enum
"""представляет собой набор символических имен (членов), привязанных к уникальным значениям

может быть повторен, чтобы вернуть его канонические (т.е. не псевдонимы) члены в порядке определения

использует синтаксис вызова для возврата членов по значению

использует синтаксис индекса для возврата членов по имени"""


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


class User_Role(enum.Enum):
    customer = 1
    executor = 2


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)  # id уникальный ключ
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, db.CheckConstraint("age > 0"))
    email = db.Column(db.Text, nullable=False)
    role = db.Column(db.Enum(User_Role), nullable=False)
    phone = db.Column(db.Integer, nullable=False)

    customers = db.relationship('Order', foreign_keys='Order.customer_id', cascade='all, delete')
    executors = db.relationship('Order', foreign_keys='Order.executor_id', cascade='all, delete')
    offers = db.relationship('Offer', foreign_keys='Offer.executor_id', cascade='all, delete')

    def t_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone,
        }


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

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    address = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, db.CheckConstraint('price > 0'))

    customer_id = db.Column(db.Integer, db.ForeignKey(f'{User.__tablename__}.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey(f'{User.__tablename__}.id'))

    customer_constraint: User = db.relationship('User', foreign_keys=[customer_id])
    executor_constraint: User = db.relationship('User', foreign_keys=[executor_id])

    orders = db.relationship('Offer', cascade='all, delete')

    def t_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "address": self.address,
            "price": self.price,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id,
            'customer_info': self.customer_constraint.t_dict(),
            'executor_info': self.customer_constraint.t_dict(),
        }


"""
ПРИМЕР
{'id': 0,
 'order_id': 36, 
 'executor_id': 10}, 
"""

"""заказчик и заказ, исполнитель связь"""


class Offer(db.Model):
    __tablename__ = 'offers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey(f'{Order.__tablename__}.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey(f'{Order.__tablename__}.id'))

    orders_constraint: Order = db.relationship('Order', foreign_keys=[order_id])
    executor_constraint: User = db.relationship('User', foreign_keys=[executor_id])

    def t_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id,
            'order_info': self.orders_constraint.t_dict(),
            'executor_info': self.executor_constraint.t_dict(),
        }
