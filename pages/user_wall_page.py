from base.base_page import BasePage
from data.links import Links
import allure
import pytest
import time

class UserWallPage(BasePage):

    _PAGE_URL_USER = Links.USER_WALL_PAGE1
    _PAGE_URL_Admin = Links.ADMIN_WALL_PAGE


    _PAGE_URL = Links.USER_WALL_PAGE
    _ADD_FRIEND_LANA_BUTTON_LOCATOR = "//div[@id = 'profile-menu']/a[contains(text(), 'Add Friend')]"
    _CANCEL_REQUEST_BUTTON_LOCATOR = "//div[@id = 'profile-menu']/a[contains(text(), 'Cancel Request')]"
    _UNFRIEND_LANA_BUTTON_LOCATOR = "//div[@id = 'profile-menu']/a[contains(text(), 'Unfriend')]"
    _TEXT_AFTER_UNFRIEND_LOCATOR = "//div[@class='ossn-system-messages-inner']"
    _MESSAGES_BUTTON_LOCATOR = "//a[@id='profile-message']"


    @allure.step("Admin send friend request user Lana lana")
    def friend_request(self):
        self.click(self._ADD_FRIEND_LANA_BUTTON_LOCATOR)
        self.wait_change_text_in_element(self._CANCEL_REQUEST_BUTTON_LOCATOR, "Cancel Request")
        self.wait_for_clickable(self._CANCEL_REQUEST_BUTTON_LOCATOR)
        text = self.get_text(self._TEXT_AFTER_UNFRIEND_LOCATOR)
        assert text == "Friend Request Sent"

    @allure.step("Admin unfriend  user Lana lana")
    def unfriend(self):
        self.click(self._UNFRIEND_LANA_BUTTON_LOCATOR)
        text = self.get_text(self._TEXT_AFTER_UNFRIEND_LOCATOR)
        assert text == "Friend request deleted!"

    def click_message_button(self):
        self.click(self._MESSAGES_BUTTON_LOCATOR)

