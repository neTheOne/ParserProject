from bs4 import BeautifulSoup
import page_saver
import time


def class_hrefs_find(html):
    '''
    Функция для извлечения ссылок на страницы классов
    :param html: html код странницы
    :return: ссылки на страницы классов
    '''
    soup = BeautifulSoup(html, "html.parser")
    all_data = soup.find_all('a', class_='tile-wrapper class')
    class_hrefs_list = []
    for hrefs in all_data:
        class_hrefs_list.append(hrefs.get("href"))

    return class_hrefs_list


def spell_hrefs_find(html):
    '''
    Функция для извлечения ссылок на страницы заклинаний
    :param html: html код странницы
    :return: лист ссылок на страницы заклинаний
    '''
    soup = BeautifulSoup(html, "html.parser")
    all_data = soup.find_all('a', class_='cards_list__item-wrapper')
    spell_hrefs_list = []
    for hrefs in all_data:
        spell_hrefs_list.append(hrefs.get("href"))

    return spell_hrefs_list


def class_info_find(class_page, spell_page):
    '''
    Функция для получения информации о классе
    :param class_page: html код странницы класса
    :param spell_page: html код странницы заклинаний класса
    :return: словарь с информацией о классе
    '''
    soup = BeautifulSoup(class_page.text, "html.parser")
    info = []
    recommend_stat = soup.find('div', class_='class__core_traits__text')
    info.append(recommend_stat)


def spell_info_find(spell_hrefs_list):
    '''
    Функция обработки страниц заклинаний
    :param spell_hrefs_list: лист со ссылками на станицы заклинаний
    :return: словарь с информацией о заклинаниях
    '''
    for href in spell_hrefs_list:
        url = "https://next.dnd.su" + href
        spell_page = page_saver.save_page_request(url)
        soup = BeautifulSoup(spell_page.text, "html.parser")
        spell_name = soup.find('h2', class_='card-title').text
        spell_name = spell_name.strip()
        range_raw = soup.find('li', class_='range')
        direct_text = range_raw.find_all(string=True, recursive=False)
        distance = ''.join(direct_text).strip()
        spell_lvl_raw = soup.find('li', class_='school_level')
        spell_lvl = spell_lvl_raw.find('a').text.strip()
        spell_description_raw = soup.find('div', itemprop='description')
        spell_description = spell_description_raw.find('p').text.strip()
        print(spell_name)
        print(distance)
        print(spell_lvl)
