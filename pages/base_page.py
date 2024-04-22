
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from data_for_test.urls import base_url

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    yield driver
    driver.quit()
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        
    # def open_page(self):
    #     self.driver.get(base_url)
    def open_page(self, url=None):
        self.driver.get(url or base_url)

    def check_menu_button_is(self, menu_item_text):
        menu_item = self.driver.find_element(By.LINK_TEXT, menu_item_text)
        assert menu_item.is_displayed(), f"Элемент меню '{menu_item_text}' не найден или не отображается."








