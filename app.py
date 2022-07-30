import service.get_product_data as get_product_data
import service.get_products_url_data as get_products_url_data
import service.insert_product_thumbnail_database as insert_product_thumbnail_database
import service.insert_price_database as insert_price_database


PRODUCT_LINKS_FILE_PATH = "resource/products_link_list.txt"
PRODUCT_DATA_FILE_PATH = "resource/product_data.txt"


def main():

    print("====== Step 1. Get Product Links From Kream! ======")
    get_products_url_data.run(PRODUCT_LINKS_FILE_PATH)

    print("====== Step 2. Get Product Data From Kream! ======")
    get_product_data.run(PRODUCT_LINKS_FILE_PATH, PRODUCT_DATA_FILE_PATH)

    print("====== Step 3. Save Product Data In Database! ======")
    insert_product_thumbnail_database.run(PRODUCT_DATA_FILE_PATH)

    print("====== Step 4. Make Dummy Price Data In Database! ======")
    insert_price_database.run()


if __name__ == "__main__":
    main()