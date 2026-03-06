from bs4 import BeautifulSoup
import page_saver
import time
import logging
import log

log.log_init()

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


def class_info_find(class_hrefs_list, spell_list):
    '''
    Функция для получения информации о классе
    :param class_hrefs_list: лист со ссылками на станицы классов
    :param spell_list: лист с заклинаниями
    :return: лист с информацией о классе
    '''
    class_list = []
    i = 0
    for href in class_hrefs_list:
        url = "https://next.dnd.su" + href
        class_page = page_saver.save_page_request(url)
        soup = BeautifulSoup(class_page.text, "html.parser")

        raw_stat = soup.find('div', class_='class__core_traits__text')
        recommend_stat = raw_stat.get_text(strip=True) # Получение рекомендованных стат

        raw_name = soup.select_one("h2.card-title a").text
        class_name = raw_name.splitlines()[1].strip() # Получение названия класса

        class_description = soup.select_one('div[data-page="lore"]').get_text(" ", strip=True)

        class_skills_raw = soup.find_all("div", class_="class__feature", attrs={"data-level": "1"})
        class_skills = {}
        for f in class_skills_raw:
            title = f.select_one("h3").get_text(strip=True)
            text = " ".join(p.get_text(strip=True) for p in f.select("p") if p.get_text(strip=True))

            class_skills[title] = text

        traits = soup.select(".class__core_traits__trait")
        hp_dice = ''
        for t in traits:
            caption = t.select_one(".class__core_traits__caption")

            if caption and caption.get_text(strip=True) == "Кость хитов":
                hp_dice = t.select_one(".class__core_traits__text").get_text(strip=True)

        spells = [] # Получение списка заклинаний доступных классу
        for spell in spell_list:
            if class_name in spell:
                spells.append(spell[1])

        class_list.append([i, recommend_stat, spells, class_name, class_description, hp_dice, class_skills])
        i += 1
        logging.info([i, recommend_stat, spells, class_name,  class_description, class_skills])

    return class_list

def spell_info_find(spell_hrefs_list):
    '''
    Функция обработки страниц заклинаний
    :param spell_hrefs_list: лист со ссылками на станицы заклинаний
    :return: словарь с информацией о заклинаниях
    '''
    spell_list = []
    i = 0
    for href in spell_hrefs_list:
        url = "https://next.dnd.su" + href
        spell_page = page_saver.save_page_request(url)
        soup = BeautifulSoup(spell_page.text, "html.parser")
        spell_name = soup.find('h2', class_='card-title').text
        spell_name = spell_name.strip() # Сохранение информации об имени заклинания
        range_raw = soup.find('li', class_='range')
        direct_text = range_raw.find_all(string=True, recursive=False)
        distance = ''.join(direct_text).strip() # Сохранение информации о дистанции заклинания
        spell_lvl_raw = soup.find('li', class_='school_level')
        spell_lvl = spell_lvl_raw.find('a').text.strip() # Сохранение информации об уровне заклинания
        spell_description_raw = soup.find('div', itemprop='description')
        spell_description = spell_description_raw.find('p').text.strip() # Сохранение описания заклинания
        type_li = soup.find('li', class_='school_level')
        links = type_li.find_all('a')
        type_text = links[1].get_text(strip=True) # Сохранение типа заклинания
        class_raw = soup.find('li', class_='class')
        spell_class = class_raw.find_all("a")[1].text # Сохранение название класса, который может использовать это заклинание
        logging.info(f"spell class {spell_class}")
        logging.info(f"Save spell {spell_name}")
        spell_list.append([i, spell_name, distance, spell_lvl, spell_description, type_text, spell_class])
        i += 1
        if i == 5:
         break
    return spell_list



