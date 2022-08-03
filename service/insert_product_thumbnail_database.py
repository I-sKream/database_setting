from tqdm import tqdm
from model.models import Product, Thumbnail
from tools.SqlAlchemyContextManager import SqlAlchemyContextManager


def read_product_from_local(file_path:str):
    line_list = []

    with open(file_path, 'r') as file:
        while True:
            line = file.readline()
            if not line: break
            line_list.append(line)
            
    return line_list


def insert_product_thumnail(brand, name_eng, name_kor, imgs) :

    with SqlAlchemyContextManager() as session:

        product = Product()
        product.brand = brand
        product.name_eng = name_eng
        product.name_kor = name_kor
        session.add(product)

        for img in imgs:
            if img == " ":
                continue
            thumbnail = Thumbnail()
            thumbnail.url = img
            thumbnail.product = product
            session.add(thumbnail)

        session.commit()


def run(product_data_path:str):

    product_list = read_product_from_local(product_data_path)

    for product in tqdm(product_list):
        brand, name_eng, name_kor, img_urls = product.split("---")
        imgs = img_urls.split(" ")
        insert_product_thumnail(brand, name_eng, name_kor, imgs)


if __name__ == "__main__":
    run("resource/product_data.txt")

