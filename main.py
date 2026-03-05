import page_saver
import page_handler
import exel_handler
from exel_handler import create_empty_excel, add_sheet_and_rows


def main():
    class_page = page_saver.save_page_selenium('https://next.dnd.su/class/')
    spells_page = page_saver.save_page_selenium('https://next.dnd.su/spells/')
    class_hrefs = page_handler.class_hrefs_find(class_page)
    spells_hrefs = page_handler.spell_hrefs_find(spells_page)
    create_empty_excel("test.xlsx")
    spell_list = list(map(lambda row: row[:-1], page_handler.spell_info_find(spells_hrefs))) # ламбда функция нужна для обрезания массива от последних элементов
    add_sheet_and_rows(create_empty_excel("test.xlsx"), "spell_sheet", spell_list)


main()
