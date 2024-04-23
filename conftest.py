from selenium import webdriver
import pytest
from time import sleep


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    sleep(3)
    yield driver
    driver.quit()
