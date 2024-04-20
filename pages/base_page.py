from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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
        
    def open_page(self):
        self.driver.get(base_url)

    def fill_form_regnum(self, regnum, regreg):
        regnum_field = self.driver.find_element(By.NAME, 'vehicle[regnum]')
        regnum_field.send_keys(regnum)
        regreg_field = self.driver.find_element(By.NAME, 'vehicle[regreg]')
        regreg_field.send_keys(regreg)
        self.driver.find_element(By.CSS_SELECTOR, 'button.button.green').click()

    def check_error_alert_text_is(self, text):
        error_message = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((
                By.XPATH, "//label[@class='error' and text()='Неверный формат госномера']"))
        ).text

        assert error_message == (text), f"Expected 'Неверный формат госномера', but got {error_message}"

    def check_added_message_text_is(self, text):
        # Ожидаем появления модального окна с текстом о дабавлении машины
        added_message = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".message .title"))
        )

        assert added_message.text == (text), f"Expected 'Отлично! Автомобиль добавлен', but got {added_message}"

    def check_menu_button_is(self, menu_item_text):
        menu_item = self.driver.find_element(By.LINK_TEXT, menu_item_text)
        assert menu_item.is_displayed(), f"Элемент меню '{menu_item_text}' не найден или не отображается."








