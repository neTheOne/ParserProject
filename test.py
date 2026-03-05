from bs4 import BeautifulSoup as BS
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import exel_handler
from exel_handler import create_empty_excel

'''
    url = "https://next.dnd.su/spells/"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    html = driver.page_source
    soup = BS(html, "html.parser")
    iph_names = soup.find_all('a', class_='cards_list__item-wrapper')
    for hrefs in iph_names:
        print(hrefs.get("href"))
'''

#soup = BeautifulSoup(page.text, "html.parser")
#all_data = soup.find('ul', class_='cards-list')
#print(all_data)
#for hrefs in all_data:


"""last_height = driver.execute_script("return document.body.scrollHeight")
while True:
	# Прокрутка вниз
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	# Пауза, пока загрузится страница.
	sleep(2)
	# Вычисляем новую высоту прокрутки и сравниваем с последней высотой прокрутки.
	new_height = driver.execute_script("return document.body.scrollHeight")
	if new_height == last_height:
		break
		print("Прокрутка завершена")
	last_height = new_height
	print("Появился новый контент, прокручиваем дальше")"""



def insert_product_db(product_name, id_number, name, description, price, count, photo_path, conn, cursor) -> None:
    """
    Функция для заполнения и обновления таблиц с информацией о продуктов в БД
    :param product_name: название продукта (овощи, фрукты, зелень и т.д
    :param cursor: параметр для подключения к БД
    :param conn: параметр для подключения к БД
    :param id_number: id конкретного овоща, фрукта или зелени
    :param name: название конкретного овоща, фрукта или зелени
    :param description: описание конкретного овоща, фрукта или зелени
    :param price: цена конкретного овоща, фрукта или зелени
    :param count: количество шт. на складе конкретного овоща, фрукта или зелени
    :param photo_path: фото конкретного овоща, фрукта или зелени
    :return: None
    """
    conn, cursor = conn, cursor
    try:
        cursor.execute(f'INSERT INTO {product_name}(id_number, name, description, price, count, photo_path) '
                       'VALUES (%s, %s, %s, %s, %s, %s) '
                       'ON CONFLICT (id_number) '
                       'DO UPDATE SET '
                       'id_number = EXCLUDED.id_number, '
                       'name = EXCLUDED.name, '
                       'description = EXCLUDED.description, '
                       'price = EXCLUDED.price, '
                       'count = EXCLUDED.count, '
                       'photo_path = EXCLUDED.photo_path;',
                       (id_number, name, description, price, count, photo_path))
        conn.commit()
        logger.info(f'Данные продукта успешно сохранены в таблицу {product_name}')
    except psycopg.Error as error:
        logger.info(f'Ошибка записи в таблицу {product_name}: {error}')


print(create_empty_excel('text.xlsx'))
