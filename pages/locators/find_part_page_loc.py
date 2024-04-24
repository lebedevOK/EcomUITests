import pytest
from selenium.webdriver.common.by import By

regnum_field_locator = (By.NAME, 'vehicle[regnum]')
regreg_field_locator = (By.NAME, 'vehicle[regreg]')
button_green_locator = (By.CSS_SELECTOR, 'button.button.green')
vin_field_locator = (By.NAME, 'vehicle[vin]')
error_regnum_message_locator = (By.XPATH, "//label[@class='error' and normalize-space(text())]")
added_message_locator = (By.CSS_SELECTOR, ".message .title")
error_vin_message_locator = (By.CSS_SELECTOR, ".errors[data-role='form.garage.errors.vin'] label[for='vehicle[vin]']")

vin_find_locator = (By.CLASS_NAME, "link-or")


class TopMenuLocators:
    ALL_CATALOGS = (By.LINK_TEXT, "Все каталоги")
    OEM_CATALOG = (By.LINK_TEXT, "OEМ-Каталог")
    PARTS_FOR_TO = (By.LINK_TEXT, "Запчасти для ТО")
    SUSPENSION = (By.LINK_TEXT, "Подвеска")
    SPARKPLUGS = (By.LINK_TEXT, "Свечи")
    FILTERS = (By.LINK_TEXT, "Фильтры")
    OILS = (By.LINK_TEXT, "Масла")
