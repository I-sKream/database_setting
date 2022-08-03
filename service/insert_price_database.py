from tqdm import tqdm
import random

from model.models import Price, User, Product
from tools.SqlAlchemyContextManager import SqlAlchemyContextManager


"""
가격대 : 가중치 * 100000 ~ 300000, 가중치는 1 ~ 9까지
판매자 : 우선 admin
사이즈 : 230 ~ 290까지 랜덤
상품 개수 : 100 ~ 200 
"""
def insert_price_database():

    with SqlAlchemyContextManager() as session:

        products = session.query(Product).all()

        for product in tqdm(products):

            price_count = random.randint(100, 200)

            sizes = [230,235,240,245,250,255,260,265,270,275,280,285,290]
            weight = random.randint(1000000, 1000000)

            for i in  range(price_count):

                rand = random.randrange(0, session.query(User).count())
                seller = session.query(User)[rand]

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
