from bs4 import BeautifulSoup as BS
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


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
