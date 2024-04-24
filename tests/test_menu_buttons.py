import pytest
from selenium.webdriver import ActionChains

from conftest import *

from pages.base_page import BasePage
from pages.locators.find_part_page_loc import TopMenuLocators


@pytest.mark.parametrize("menu_item_locator", [
    TopMenuLocators.ALL_CATALOGS,
    # TopMenuLocators.OEM_CATALOG,
    # TopMenuLocators.PARTS_FOR_TO,
    # TopMenuLocators.SUSPENSION,
    # TopMenuLocators.SPARKPLUGS,
    # TopMenuLocators.FILTERS,
    # TopMenuLocators.OILS,
])
def test_menu_items_presence(find_part_page, menu_item_locator):
    # инициализация страницы через find_part_page, а не через base_page
    find_part_page.open_page()

    find_part_page.close_modal()

    find_part_page.check_menu_button_is(menu_item_locator)
