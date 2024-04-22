from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from data_for_test.urls import login_url
from data_for_test.users import email_unregistered_user, password_unregistered_user


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(login_url)

    def fill_form_login(self, email, password):
        email_field = self.driver.find_element(By.CSS_SELECTOR, "input#user_email")
        email_field.send_keys(email)
        password_field = self.driver.find_element(By.CSS_SELECTOR, "input#user_password")
        password_field.send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Войти']").click()

    def check_error_alert_text_is(self, text):
        error_message_element = self.driver.find_element(By.XPATH,
                                                    "//div[@class='text_to_center']/p[@class='alert' and contains(text(), 'Неверный Email или пароль.')]")
        error_message = error_message_element.text
        assert error_message == text, f"Expected '{text}', but got '{error_message}'"
