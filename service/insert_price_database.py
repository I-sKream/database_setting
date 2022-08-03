from tqdm import tqdm
import random

from model.models import Price, User, Product
import service.insert_user_database as insert_user_database
from tools.SqlAlchemyContextManager import SqlAlchemyContextManager


def get_random_user(session):
    rand_user = random.randrange(0, session.query(User).count())
    user = session.query(User)[rand_user]
    return user


def insert_price_database():

    with SqlAlchemyContextManager() as session:

        products = session.query(Product).all()

        for product in tqdm(products):

            price_count = random.randint(100, 200)

            sizes = [230,235,240,245,250,255,260,265,270,275,280,285,290]
            weight = random.randint(100000, 1000000)

            for i in  range(price_count):
                
                seller = get_random_user(session)

                size = random.choice(sizes)
                _price = random.randrange(1 * weight, 5 * weight, 10000)

                price = Price()

                price.price = _price
                price.product = product
                price.seller = seller
                price.size = size

                session.add(price)

            session.commit()


def run():
    insert_price_database()


if __name__ == "__main__":
    run()
