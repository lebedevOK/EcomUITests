from selenium.webdriver.remote.webdriver import WebDriver
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from data_for_test.urls import base_url


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self, url=None):
        self.driver.get(url or base_url)

    def check_menu_button_is(self, menu_item_text):
        menu_item = self.driver.find_element(By.LINK_TEXT, menu_item_text)
        assert menu_item.is_displayed(), f"Элемент меню '{menu_item_text}' не найден или не отображается."
