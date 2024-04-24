from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from data_for_test.urls import login_url
from pages.base_page import BasePage
from pages.locators.login_page_loc import *


class LoginPage(BasePage):

    def fill_form_login(self, email, password):
        email_field = self.find(email_field_locator)
        email_field.send_keys(email)
        password_field = self.find(password_field_locator)
        password_field.send_keys(password)
        button_submit = self.find(button_submit_locator)
        button_submit.click()

    def check_error_alert_text_is(self, text):
        """
        Ожидаем появления модального окна с текстом 'Неверный логин или пароль'
        """
        error_message_element = self.find(error_message_locator)
        error_message = error_message_element.text
        assert error_message == text, f"Expected '{text}', but got '{error_message}'"

    def check_login_alert_text_is(self, text):
        """Ожидаем появления модального окна с текстом 'Вход в систему выполнен.'"""
        login_notice = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(login_notice_locator))

        actual_message = login_notice.text
        assert actual_message == (text), f"Expected message to be '{text}', but got '{actual_message}'"
