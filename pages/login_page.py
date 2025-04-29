from base.base_page import BasePage
from data.links import Links
import allure
import pytest
import time

class LoginPage(BasePage):

    _PAGE_URL = Links.LOGIN_PAGE
    _USERNAME_LOCATOR = "//input[@name='username']"
    _PASSWORD_LOCATOR = "//input[@name='password']"
    _LOGIN_BUTTON_LOCATOR = "//input[@value='Login']"
    _RESET_PASSWORD_LOCATOR = "//a[contains(text(),'Reset')]"
    _ERROR_LABEL_LOCATOR = "//div[@class='alert alert-danger']/strong"
    @allure.step("Fill username")
    def username_fill(self, login):
        self.clear(self._USERNAME_LOCATOR).send_keys(login)
        user_name = self.find(self._USERNAME_LOCATOR)
        assert login in user_name.get_attribute("value")

    @allure.step("Fill password")
    def password_fill(self, password):
        self.clear(self._PASSWORD_LOCATOR).send_keys(password)

    @allure.step("Click login button")
    def click_login_button(self):
        self.click(self._LOGIN_BUTTON_LOCATOR)
        assert self.driver.current_url == Links.NEWSFEED_PAGE

    @allure.step("Click reset password button")
    def click_reset_password(self):
        self.click(self._RESET_PASSWORD_LOCATOR)
        assert self.driver.current_url == Links.RESETLOGIN_PAGE

    @allure.step("Login us user")
    def login_as_user(self):
        self.clear(self._USERNAME_LOCATOR).send_keys(self.credentials.LOGIN_USER)
        self.clear(self._PASSWORD_LOCATOR).send_keys(self.credentials.PASSWORD_USER)
        self.click(self._LOGIN_BUTTON_LOCATOR)

    @allure.step("Login us admin")
    def login_as_admin(self):
        self.clear(self._USERNAME_LOCATOR).send_keys(self.credentials.LOGIN_ADMIN)
        self.clear(self._PASSWORD_LOCATOR).send_keys(self.credentials.PASSWORD_ADMIN)
        self.click(self._LOGIN_BUTTON_LOCATOR)
        assert self.driver.current_url == Links.NEWSFEED_PAGE

    def login_as(self, role="user"):
        with allure.step(f"Login as: '{role}'"):
            if role == "admin":
                login = self.credentials.LOGIN_ADMIN
                password = self.credentials.PASSWORD_ADMIN
            else:
                login = self.credentials.LOGIN_USER
                password = self.credentials.PASSWORD_USER
            self.clear(self._USERNAME_LOCATOR).send_keys(login)
            self.clear(self._PASSWORD_LOCATOR).send_keys(password)
            self.click(self._LOGIN_BUTTON_LOCATOR)

    @allure.step("Login in account with differt user")
    def login_in_account_with_different_user(self, login, password, error_message, expected_result):
        self.clear(self._USERNAME_LOCATOR).send_keys(login)
        self.clear(self._PASSWORD_LOCATOR).send_keys(password)
        self.click(self._LOGIN_BUTTON_LOCATOR)
        if not expected_result:  # если expected_result не True, тогда проверяем тест ошибки
            assert self.driver.find_element(*self._ERROR_LABEL_LOCATOR).text == error_message
        else:
            assert self.driver.current_url == Links.NEWSFEED_PAGE
