from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver): # конструктор, который принимает driver — экземпляр webdriver
        self.driver = driver
        self.base_url = "https://yandex.ru/"

    def find_element(self, locator, time=10): # ищет один элемент и возвращает его
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10): # ищет элементы и возвращает список
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self): # переходит на сайт
        return self.driver.get(self.base_url)

    def get_current_url(self): # получает url последней открытой вкладки
        handles = self.driver.window_handles
        size = len(handles)
        self.driver.switch_to.window(handles[size-1])
        return self.driver.current_url