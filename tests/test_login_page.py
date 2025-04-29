import time

import allure
import pytest

from base.base_test import BaseTest
from data.credentials import Credentials

@allure.epic("Account")
class TestLoginPage(BaseTest):


    @allure.title("Login in account user and admin")
    @pytest.mark.parametrize('login,password', [
        (Credentials.LOGIN_USER, Credentials.PASSWORD_USER),
        (Credentials.LOGIN_ADMIN, Credentials.PASSWORD_ADMIN)
    ])
    def test_login(self, login, password):
        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().username_fill(login)
        self.login_page().password_fill(password)
        self.login_page().click_login_button()


    @allure.title("Login in account user")
    def test_login_as_user(self):
        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as_user()

    @allure.title("Login in account admin")
    def test_login_as_admin(self):
        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as_admin()
        # self.login_page().top_bar_messages.open_messages()
        # self.login_page().top_bar_messages.name_send_last_massages()

    @allure.title("Login as ")
    def test_login_as(self):
        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as("user")

    @allure.title("Login in account with different user")
    @pytest.mark.parametrize('login,password, error_message,expected_result', [
        (Credentials.LOGIN_USER, Credentials.PASSWORD_USER, None, True),
        (Credentials.LOGIN_ADMIN, Credentials.PASSWORD_ADMIN, None, True),
        # негативные тесты
        ("invalid user", Credentials.PASSWORD_USER, "Invalid username or password!", False),
        (Credentials.LOGIN_USER, "invalid password", "Invalid username or password!", False),
        ("invalid user", "invalid password", "Invalid username or password!", False)
    ])
    def test_login_in_account_with_different_user(self, login, password, error_message, expected_result):
        self.login_page().open()
        self.login_page().login_in_account_with_different_user(login, password, error_message, expected_result)
