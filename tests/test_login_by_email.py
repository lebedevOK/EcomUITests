from selenium.webdriver import ActionChains

from conftest import driver
from data_for_test.urls import login_url
from data_for_test.users import email_unregistered_user, password_unregistered_user

from pages.login_page import LoginPage
def test_unregistered_user(driver):
    login_page = LoginPage(driver)
    login_page.open_page()

    login_page.fill_form_login(email_unregistered_user, password_unregistered_user)
    login_page.check_error_alert_text_is('Неверный Email или пароль.')