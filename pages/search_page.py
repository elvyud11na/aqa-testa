import allure
from base.base_page import BasePage
from selenium.webdriver import Keys
from data.links import Links
from selenium.webdriver.support import expected_conditions as EC
import time

class SearchPage(BasePage):
    #_PAGE_URL = Links.SEARCH_PAGE

    _ADD_FRIEND_BUTTON = "//div[@class='right users-list-controls']/a"
    _CANSEL_REQUEST_BUTTON = "//div[@class='right users-list-controls']/a"
    _TEXT_AFTER_CLICK_BUTTON_LOCATOR = "//div[@class='ossn-system-messages-inner']"

    @allure.step("Click button 'Add friend'")
    def click_add_friend(self):
        self.click(self._ADD_FRIEND_BUTTON)
        text = self.get_text(self._TEXT_AFTER_CLICK_BUTTON_LOCATOR)
        assert text == "Friend Request Sent"

    @allure.step("Click button 'Cansel_request'")
    def click_cansel_request(self):
        self.click(self._CANSEL_REQUEST_BUTTON)
        text = self.get_text(self._TEXT_AFTER_CLICK_BUTTON_LOCATOR)
        print(text)
        assert text == "Friend request deleted!"


