from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from data_for_test.urls import base_url
from pages.locators.find_part_page_loc import TopMenuLocators


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self, url=None):
        self.driver.get(url or base_url)

    def close_modal(self):
        # Создаем объект ActionChains
        actions = ActionChains(self.driver)
        # Перемещаем курсор в левый верхний угол окна и совершаем клик с отступом в 10 пикселей
        actions.move_by_offset(10, 10).click().perform()

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def check_menu_button_is(self, menu_item_locator):
        menu_item = self.driver.find_element(*menu_item_locator)
        assert menu_item.is_displayed(), f"Элемент меню '{menu_item_locator}' не найден или не отображается."
