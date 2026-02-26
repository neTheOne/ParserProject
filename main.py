import page_saver
import page_handler

def main():
    class_page = page_saver.save_page_selenium('https://next.dnd.su/class/')
    spells_page = page_saver.save_page_selenium('https://next.dnd.su/spells/')
    class_hrefs = page_handler.class_hrefs_find(class_page)
    spells_hrefs = page_handler.spell_hrefs_find(spells_page)
    page_handler.spell_info_find(spells_hrefs)


main()