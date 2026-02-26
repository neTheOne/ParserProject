import requests
import page_saver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def save_page_request(url):
    '''
    Функция для получения html кода страницы
    :param url: url страницы для которой нужно получить html код
    :return: html код
    '''
    while True:
        page = requests.get(url)
        time.sleep(1.5)
        if page.status_code == 200:
            print(page.status_code)
            return page
        print(page.status_code)


def save_page_selenium(url):
    '''
    Функция для получения html кода страницы
    :param url: url страницы для которой нужно получить html код
    :return: html код
    '''
    driver = webdriver.Chrome()
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    page = driver.page_source

    return page