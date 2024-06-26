from conftest import *
from data_for_test.urls import login_url
from data_for_test.users import email_unregistered_user, password_unregistered_user, email_registered_user, \
    password_registered_user

from pages.login_page import LoginPage


def test_unregistered_user(login_page):
    login_page.open_page(login_url)

    login_page.fill_form_login(email_unregistered_user, password_unregistered_user)
    login_page.check_error_alert_text_is('Неверный Email или пароль.')


def test_registered_user(login_page):
    login_page.open_page(login_url)

    login_page.fill_form_login(email_registered_user, password_registered_user)
    login_page.check_login_alert_text_is('Вход в систему выполнен.')
