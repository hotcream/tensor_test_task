from YandexPages import SearchHelper
import time
import pytest
from selenium.webdriver.common.keys import Keys
# Установите pytest-html а затем запустите тест с параметром --html=pytest_report.html

def test_yandex_search(browser):
    '''Первый тест'''
    yandex_page = SearchHelper(browser) 
    yandex_page.go_to_site() # зайти на yandex.ru
    search_field = yandex_page.find_search_field() # проверить наличие поля поиска
    yandex_page.enter_word("тензор") # ввести в поиск Тензор
    assert yandex_page.get_suggest()  # проверяет, что появилась таблица с подсказками 
    search_field.send_keys(Keys.RETURN)  # нажимает Enter 
    results = yandex_page.get_search_results() 
    assert len(results) > 0 # при нажатии Enter появляется таблица результатов поиска
    
    included_link = False 
    for x in results[:6]:
        if "tensor.ru" in x.text:
            included_link = True
    assert included_link # В первых 5 результатах есть ссылка на tensor.ru

def test_yandex_pictures(browser):
    '''Второй тест'''
    yandex_page = SearchHelper(browser) 
    yandex_page.go_to_site() # зайти на yandex.ru
    element = yandex_page.get_bar_element("Картинки") # получает ссылку на категорию
    assert element # Ссылка «Картинки» присутствует на странице
    element.click() # кликает ссылку
    current_url = yandex_page.get_current_url() # получает текущий url
    assert "https://yandex.ru/images/" in current_url # проверяет, что перешли на url https://yandex.ru/images/ 
    img_category_link = yandex_page.get_image_categories() # получает ссылку на первую категорию 
    img_category_link[0].click()  # открывает первую категорию 
    img_category_name = img_category_link[0].text  # получает имя категории
    assert yandex_page.check_opened_category()  # проверяет что категория открылась 
    description = yandex_page.get_description() # получает описание страницы из head
    assert img_category_name in description.get_attribute('content') # в строке поиска верный текст 
    images_list = yandex_page.find_images() # получает список картинок
    images_list[0].click() # открывает первую картинку
    time.sleep(1) # ждет прогрузки картинки
    first_image = yandex_page.get_opened_image() # получает элемент 
    assert first_image # проверяет что картинка открылась
    first_image = first_image.get_attribute('src') # получает url первого изобажения
    yandex_page.find_dir_button('next').click() # нажимает кнопку вперед
    time.sleep(1) # ждет прогрузки картинки 
    second_image = yandex_page.get_opened_image() # получает элемент
    assert second_image # проверяет что картинка открылась
    second_image = second_image.get_attribute('src') # получает url второго изображения
    assert first_image != second_image # проверяет изменение картинки
    yandex_page.find_dir_button('prev').click() # нажимает кнопку назад
    time.sleep(1) # ждет прогрузки картинки
    assert first_image == yandex_page.get_opened_image().get_attribute('src') # проверяет, что этоодно и то же изображение