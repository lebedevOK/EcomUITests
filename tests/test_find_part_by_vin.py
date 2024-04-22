from selenium.webdriver import ActionChains, Keys

from conftest import driver
from selenium.webdriver.common.by import By

from data_for_test.vins import vin, incorrect_vin, not_found_vin
from pages.find_part_page import FindPartPage


def test_incorrect_vin(driver):
    find_part_page = FindPartPage(driver)
    find_part_page.open_page()

    # Для закрытия модалки Создаем объект ActionChains,
    # перемещаем курсор в левый верхний угол окна и совершаем клик с отступом в 10 пикселей
    actions = ActionChains(driver)
    actions.move_by_offset(10, 10).click().perform()

    # Переключаемся в поиск по VIN
    driver.find_element(By.CLASS_NAME, "link-or").click()

    find_part_page.fill_form_vin(incorrect_vin)
    find_part_page.check_error_alert_vin_text_is("Неверный формат VIN-номера")


def test_correct_vin(driver):
    find_part_page = FindPartPage(driver)
    find_part_page.open_page()

    # Для закрытия модалки Создаем объект ActionChains,
    # перемещаем курсор в левый верхний угол окна и совершаем клик с отступом в 10 пикселей
    actions = ActionChains(driver)
    actions.move_by_offset(10, 10).click().perform()

    # Переключаемся в поиск по VIN
    driver.find_element(By.CLASS_NAME, "link-or").click()

    find_part_page.fill_form_vin(vin)
    find_part_page.check_added_message_text_is("Отлично! Автомобиль добавлен")
