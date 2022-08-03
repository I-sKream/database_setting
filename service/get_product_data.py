from selenium.webdriver.common.by import By
from tqdm import tqdm

from tools.SeleniumContextManager import SeleniumContextManager


def read_product_url_data_from_local(file_path:str):

    line_list = []

    with open(file_path, 'r') as file:
        while True:
            line = file.readline()
            if not line: break
            line_list.append(line)
    
    return line_list


def save_product_data_in_local(file_path:str, data_list:list):

    with open(file_path, 'w') as file:
        while data_list:
            data = data_list.pop()
            file.write(data + "\n")


def get_product_data(product_url:str) -> tuple:

    with SeleniumContextManager() as driver:

        driver.get(product_url)

        driver.implicitly_wait(5)

        brand = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div/a").text

        name_eng = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div/p[1]").text

        name_kor = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div/p[2]").text

        imgs = driver.find_elements(By.XPATH, "/html/body/div/div/div/div[2]/div[1]/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/picture/img")

        img_urls = []

        if not imgs:
            img = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/picture/img")
            img_urls.append(img.get_attribute("src"))
        else:
            for img in imgs : 
                img_urls.append(img.get_attribute("src"))

        return (brand, name_eng, name_kor, img_urls)


def run(products_url_path:str, product_data_path:str):
    url_list = read_product_url_data_from_local(products_url_path)

    data_list = []
    for url in tqdm(url_list):
        brand, name_eng, name_kor, img_urls = get_product_data(url)
        urls = " ".join(img_urls)
        if(brand and name_eng and name_kor and urls):
            data_list.append(brand + "---" + name_eng + "---" + name_kor + "---" + urls)
    
    save_product_data_in_local(product_data_path, data_list)


if __name__ == "__main__":
    run("resource/products_link_list.txt", "resource/product_data.txt")




