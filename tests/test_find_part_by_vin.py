from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from selenium.webdriver.common.by import By
from time import sleep
import time

from data_for_test.vins import vin, incorrect_vin, not_found_vin
from data_for_test.urls import base_url


def test_incorrect_vin(driver):
    # Засекаем время старта
    start_time = time.time()

    driver.get(base_url)

    # Создаем объект ActionChains
    actions = ActionChains(driver)
    # Перемещаем курсор в левый верхний угол окна и совершаем клик с отступом в 10 пикселей
    actions.move_by_offset(10, 10).click().perform()

    # Переключаемся в поиск по VIN
    driver.find_element(By.CLASS_NAME, "link-or").click()

    # Вводим некорректный VIN
    vin_field = driver.find_element(By.NAME, 'vehicle[vin]')
    vin_field.send_keys(incorrect_vin)

    # Нажимаем кнопку добавления автомобиля
    driver.find_element(By.CSS_SELECTOR, 'button.button.green').click()
    sleep(3)

    # Находим ошибку при неверном формате VIN-номера
    error_message_vin = driver.find_element(By.CSS_SELECTOR,
                                            ".errors[data-role='form.garage.errors.vin'] label[for='vehicle[vin]']").text

    assert error_message_vin == "Неверный формат VIN-номера", f"Expected 'Неверный формат VIN-номера', but got {error_message_vin}"

    # Вычисляем и печатаем прошедшее время
    elapsed_time = time.time() - start_time
    print(f"Время выполнения теста test_incorrect_vin: {elapsed_time} секунд.")
