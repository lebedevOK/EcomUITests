from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from selenium.webdriver.common.by import By
from time import sleep
import time

from data_for_test.regnum import uncorrect_regnum, uncorrect_regreg, not_found_regnum, not_found_regreg, regnum, regreg
from data_for_test.urls import base_url


def test_incorrect_regnum(driver):
    driver.get(base_url)

    # Создаем объект ActionChains
    actions = ActionChains(driver)
    # Перемещаем курсор в левый верхний угол окна и совершаем клик с отступом в 10 пикселей
    actions.move_by_offset(10, 10).click().perform()

    regnum_field = driver.find_element(By.NAME, 'vehicle[regnum]')
    regnum_field.send_keys(uncorrect_regnum)
    regreg_field = driver.find_element(By.NAME, 'vehicle[regreg]')
    regreg_field.send_keys(uncorrect_regreg)

    # Нажимаем кнопку добавления автомобиля
    driver.find_element(By.CSS_SELECTOR, 'button.button.green').click()

    # Явное ожидание для текста ошибки
    error_message = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((
            By.XPATH, "//label[@class='error' and text()='Неверный формат госномера']"))
    ).text

    assert error_message == "Неверный формат госномера", f"Expected 'Неверный формат госномера', but got {error_message}"
