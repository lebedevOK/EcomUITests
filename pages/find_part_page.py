from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators.find_part_page_loc import *



class FindPartPage(BasePage):
    def fill_form_regnum(self, regnum, regreg):
        regnum_field = self.find(regnum_field_locator)
        regnum_field.send_keys(regnum)
        regreg_field = self.find(regreg_field_locator)
        regreg_field.send_keys(regreg)
        button_green = self.find(button_green_locator)
        button_green.click()

    def switch_to_vin_search(self):
        # Переключаемся в поиск по VIN
        vin_search_element = self.driver.find_element(*vin_find_locator)
        vin_search_element.click()

    def fill_form_vin(self, vin):
        vin_field = self.find(vin_field_locator)
        vin_field.send_keys(vin)
        button_green = self.find(button_green_locator)
        button_green.click()
    def check_error_alert_regnum_text_is(self, text):
        """
        Ожидаем появления модального окна с текстом 'Неверный формат госномера'
        """
        error_regnum_message = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located(error_regnum_message_locator)
        ).text

        assert error_regnum_message == text, f"Expected '{text}', but got {error_regnum_message}"

    def check_added_message_text_is(self, text):
        """
        Ожидаем появления модального окна с текстом 'Отлично! Автомобиль добавлен'
        """
        added_message = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(added_message_locator)
        )
        assert added_message.text == text, f"Expected '{text}', but got {added_message}"

    def check_error_alert_vin_text_is(self, text):
        """
        Ожидаем появления модального окна с текстом 'Неверный формат VIN-номера'
        """
        # Находим ошибку при неверном формате VIN-номера
        error_vin_message = self.find(error_vin_message_locator).text
        assert error_vin_message == text, f"Expected '{text}', but got {error_vin_message}"
