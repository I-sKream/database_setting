from datetime import date, timedelta
import random
import tqdm

from model.models import Order, Price, User
from tools.SqlAlchemyContextManager import SqlAlchemyContextManager


def get_random_user(session):
    rand_user = random.randrange(0, session.query(User).count())
    buyer = session.query(User)[rand_user]
    return buyer


def get_ramdom_date():
    today = date.today()
    rand_date = random.randint(-7, 7)
    date_diff = timedelta(days=rand_date)
    return today - date_diff


def insert_order_database() :

    with SqlAlchemyContextManager() as session:

        prices = session.query(Price).all()

        for price in tqdm(prices):
            rand = random.randint(1, 10)
            if rand != 5:
                buyer = get_random_user(session)
                date = get_ramdom_date()

                order = Order()
                order.buyer = buyer
                order.price = price
                order.date = date
                session.add(order)

            session.commit()


def run():
    insert_order_database()