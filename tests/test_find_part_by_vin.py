from selenium.webdriver import ActionChains, Keys

from conftest import *

from data_for_test.vins import vin, incorrect_vin, not_found_vin
from pages.find_part_page import FindPartPage
from pages.locators.find_part_page_loc import *


def test_incorrect_vin(find_part_page):
    # find_part_page = FindPartPage(driver)
    find_part_page.open_page()

    find_part_page.close_modal()
    find_part_page.switch_to_vin_search()

    find_part_page.fill_form_vin(incorrect_vin)
    find_part_page.check_error_alert_vin_text_is("Неверный формат VIN-номера")


def test_correct_vin(find_part_page):
    # find_part_page = FindPartPage(driver)
    find_part_page.open_page()

    find_part_page.close_modal()
    find_part_page.switch_to_vin_search()

    find_part_page.fill_form_vin(vin)
    find_part_page.check_added_message_text_is("Отлично! Автомобиль добавлен")
