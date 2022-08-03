import bcrypt
import string
from tqdm import tqdm
import random

from model.models import User
from tools.SqlAlchemyContextManager import SqlAlchemyContextManager


def make_random_user_name():
    
    first_name_samples = "김이박최정강조윤장임"
    middle_name_samples = "민서예지도하주윤채현지"
    last_name_samples = "준윤우원호후서연아은진"

    name = ""
    name += random.choice(first_name_samples)
    name += random.choice(middle_name_samples)
    name += random.choice(last_name_samples)
    
    return name


def make_dummy_user():

    user = User()
    user.id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    user.password = bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    user.nickname = make_random_user_name()

    return user


def insert_user_database(userList) :

    with SqlAlchemyContextManager() as session:

        print("===== Insert Dummy Users ===== ")
        for user in tqdm(userList):
            session.add(user)

        session.commit()


def run():

    user_list = []
    
    print("===== Make Dummy Users ===== ")
    for i in tqdm(range(500)):
        user = make_dummy_user()
        user_list.append(user)

    insert_user_database(user_list)