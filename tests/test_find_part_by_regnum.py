from selenium.webdriver import ActionChains

from conftest import driver
from data_for_test.regnum import uncorrect_regnum, uncorrect_regreg, not_found_regnum, not_found_regreg, regnum, regreg

from pages.base_page import BasePage
from pages.find_part_page import FindPartPage


def test_incorrect_regnum(driver):
    find_part_page = FindPartPage(driver)
    find_part_page.open_page()

    # Для закрытия модалки Создаем объект ActionChains,
    # перемещаем курсор в левый верхний угол окна и совершаем клик с отступом в 10 пикселей
    actions = ActionChains(driver)
    actions.move_by_offset(10, 10).click().perform()

    find_part_page.fill_form_regnum(uncorrect_regnum, uncorrect_regreg)
    find_part_page.check_error_alert_regnum_text_is("Неверный формат госномера")


def test_correct_regnum(driver):
    find_part_page = FindPartPage(driver)
    find_part_page.open_page()

    # Для закрытия модалки Создаем объект ActionChains,
    # перемещаем курсор в левый верхний угол окна и совершаем клик с отступом в 10 пикселей
    actions = ActionChains(driver)
    actions.move_by_offset(10, 10).click().perform()

    find_part_page.fill_form_regnum(regnum, regreg)
    find_part_page.check_added_message_text_is("Отлично! Автомобиль добавлен")
