from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from data_for_test.urls import login_url
from pages.base_page import BasePage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class LoginPage(BasePage):


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

    def check_login_alert_text_is(self, text):
        login_notice = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='text_to_center']/p[@class='notice' and text()='Вход в систему выполнен.']"))
        )
        actual_message = login_notice.text
        assert actual_message == (text), f"Expected message to be '{text}', but got '{actual_message}'"
