from selenium import webdriver
import pytest
from time import sleep
from pages.find_part_page import FindPartPage
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    sleep(3)
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def find_part_page(driver):
    return FindPartPage(driver)
