import pytest
from selenium.webdriver import ActionChains

from conftest import driver

from pages.base_page import BasePage


@pytest.mark.parametrize("menu_item_text", [
    "Все каталоги",
    "OEМ-Каталог",
    "Запчасти для ТО",
    "Подвеска",
    "Свечи",
    "Фильтры",
    "Масла",
    "Амортизаторы",
    "Лампы"
])
def test_menu_items_presence(driver, menu_item_text):
    base_page = BasePage(driver)
    base_page.open_page()

    # Для закрытия модалки Создаем объект ActionChains,
    # перемещаем курсор в левый верхний угол окна и совершаем клик с отступом в 10 пикселей
    actions = ActionChains(driver)
    actions.move_by_offset(10, 10).click().perform()

    base_page.check_menu_button_is(menu_item_text)
