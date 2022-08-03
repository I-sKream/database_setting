import time

from selenium.webdriver.common.by import By

from project_setting import INFINITE_SCROLL_COUNT
from tools.SeleniumContextManager import SeleniumContextManager


def save_products_url_in_local(file_path:str, link_list):

    with open(file_path, 'w') as file:
        for link in link_list:
            file.write(link + " \n")


def get_products_url_data():

    with SeleniumContextManager() as driver:

        driver.get("https://kream.co.kr/search?category_id=34&sort=popular&per_page=40")

        driver.implicitly_wait(5)

        scroll_count = INFINITE_SCROLL_COUNT

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while scroll_count > 0:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
            time.sleep(2)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break

            last_height = new_height

            scroll_count -= 1

        links = driver.find_elements(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div/div/a")

        link_list = []
        for target in links:
            link = target.get_attribute("href")
            if link is not None:
                link_list.append(link)

        return link_list


def run(file_path:str):
    link_list = get_products_url_data()
    save_products_url_in_local(file_path,link_list)


if __name__ == "__main__":
    run("resource/products_link_list.txt")
