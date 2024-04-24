
from conftest import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_incorrect_regnum(driver):
    driver.get("https://parterra.ru/")

    # Инициализация WebDriver
    driver = webdriver.Chrome()  # Или любой другой браузер
    driver.get("https://parterra.ru/")  # Замените URL на нужный

    # Ожидание появления iframe на странице
    WebDriverWait(driver, 3).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe_selector")))

    # Теперь когда мы находимся внутри iframe, то можем искать элементы внутри него
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, "confirm-city")))

    # Нажатие на кнопку "Да"
    button_yes = driver.find_element(By.CSS_SELECTOR, ".confirm-city .butn.yellow")
    button_yes.click()

    # После взаимодействия с модальным окном внутри iframe, вернитесь к основному содержимому страницы
    driver.switch_to.default_content()

    regnum_field = driver.find_element(By.NAME, 'vehicle[regnum]')
    regnum_field.send_keys('555')

    # regnum_field = driver.find_element(By.NAME, 'vehicle[regnum]')
    # regnum_field.send_keys(uncorrect_regnum)
    # regreg_field = driver.find_element(By.NAME, 'vehicle[regreg]')
    # regreg_field.send_keys(uncorrect_regreg)
    #
    # # Нажимаем кнопку добавления автомобиля
    # driver.find_element(By.CSS_SELECTOR, 'button.button.green').click()

    base_page.check_error_alert_text_is("Неверный формат госномера")
    # # Явное ожидание для текста ошибки
    # error_message = WebDriverWait(driver, 1).until(
    #     EC.presence_of_element_located((
    #         By.XPATH, "//label[@class='error' and text()='Неверный формат госномера']"))
    # ).text
    #
    # assert error_message == "Неверный формат госномера", f"Expected 'Неверный формат госномера', but got {error_message}"
