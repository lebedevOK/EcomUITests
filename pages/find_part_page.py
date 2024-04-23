from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class FindPartPage(BasePage):
    def fill_form_regnum(self, regnum, regreg):
        regnum_field = self.driver.find_element(By.NAME, 'vehicle[regnum]')
        regnum_field.send_keys(regnum)
        regreg_field = self.driver.find_element(By.NAME, 'vehicle[regreg]')
        regreg_field.send_keys(regreg)
        self.driver.find_element(By.CSS_SELECTOR, 'button.button.green').click()

    def fill_form_vin(self, vin):
        vin_field = self.driver.find_element(By.NAME, 'vehicle[vin]')
        vin_field.send_keys(vin)
        self.driver.find_element(By.CSS_SELECTOR, 'button.button.green').click()

    def check_error_alert_regnum_text_is(self, text):
        """
        Ожидаем появления модального окна с текстом 'Неверный формат госномера'
        """
        error_message = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((
                By.XPATH, "//label[@class='error' and normalize-space(text())]"))
        ).text

        assert error_message == text, f"Expected '{text}', but got {error_message}"

    def check_added_message_text_is(self, text):
        """
        Ожидаем появления модального окна с текстом 'Отлично! Автомобиль добавлен'
        """
        added_message = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".message .title"))
        )

        assert added_message.text == text, f"Expected '{text}', but got {added_message}"

    def check_error_alert_vin_text_is(self, text):
        """
        Ожидаем появления модального окна с текстом 'Неверный формат VIN-номера'
        """
        # Находим ошибку при неверном формате VIN-номера
        error_message_vin = self.driver.find_element(By.CSS_SELECTOR,
                                                     ".errors[data-role='form.garage.errors.vin'] label[for='vehicle[vin]']").text

        assert error_message_vin == text, f"Expected '{text}', but got {error_message_vin}"
