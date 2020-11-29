from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

class YandexSeacrhLocators:

    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_RESULTS = (By.CSS_SELECTOR, ".organic")
    LOCATOR_YANDEX_SUGGEST = (By.CSS_SELECTOR, ".body_search_yes")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".services-new__item-title")
    LOCATOR_IMAGE_CATEGORIES = (By.CSS_SELECTOR, ".PopularRequestList-Item")    
    LOCATOR_OPENED_CATEGORY = (By.CSS_SELECTOR, ".justifier__item")
    LOCATOR_YANDEX_IMAGES = (By.CSS_SELECTOR, ".serp-item__link")
    LOCATOR_OPENED_CATEGORY_NAME = (By.NAME, "description")
    LOCATOR_OPENED_IMAGE = (By.CSS_SELECTOR, ".MMImage-Origin")
    LOCATOR_BUTTON_NEXT = (By.CSS_SELECTOR, ".CircleButton_type_next")
    LOCATOR_BUTTON_PREV = (By.CSS_SELECTOR, ".CircleButton_type_prev")

class SearchHelper(BasePage):

    def find_search_field(self): # ищет элемент строки поиска
        self.search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)        
        return self.search_field

    def enter_word(self, word): # кликает и вводит в поиск необходимое слово
        self.search_field.click()
        self.search_field.send_keys(word)
        return self.search_field

    def get_suggest(self): # возвращает таблицу с подсказками
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SUGGEST)

    def get_search_results(self): # возвращает таблицу результатов поиска
        return self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_RESULTS)

    def get_navigation_bar(self): # ищет элементы навигации 
        all_navigation_list = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR)
        nav_bar_menu = {x.text: x for x in all_navigation_list if len(x.text) > 0}
        # Создает словарь и фильтрует по условию. Если длина строки больше нуля, то добавляет элементы к словарю.
        return nav_bar_menu 

    def get_bar_element(self, name): # получает ссылку на категорию
        nav_bar_menu = self.get_navigation_bar()
        value = nav_bar_menu.get(name)
        if value:
            return value

    def get_image_categories(self): # ищет все категории 
        all_image_category_list = self.find_elements(YandexSeacrhLocators.LOCATOR_IMAGE_CATEGORIES)       
        img_cat_list = [x for x in all_image_category_list if len(x.text) > 0]
        return img_cat_list

    def check_opened_category(self): # проверяет открытые категории
        opened_cat_list = self.find_elements(YandexSeacrhLocators.LOCATOR_OPENED_CATEGORY)
        if len(opened_cat_list) > 0 :
            return True
        return False      
        
    def get_description(self): # возвращает описание страницы из head
        return self.find_element(YandexSeacrhLocators.LOCATOR_OPENED_CATEGORY_NAME)

    def find_images(self): # ищет картинки на странице категории
        return self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_IMAGES)

    def get_opened_image(self): # возвращает элемент открытой картинки
        return self.find_element(YandexSeacrhLocators.LOCATOR_OPENED_IMAGE)

    def find_dir_button(self, dir_name): # ищет кнопки вперед и назад
        if dir_name == 'next' :
            return self.find_element(YandexSeacrhLocators.LOCATOR_BUTTON_NEXT)
        elif dir_name == 'prev' :
            return self.find_element(YandexSeacrhLocators.LOCATOR_BUTTON_PREV)
        else:
            return False