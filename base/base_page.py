import allure

from base.base_components.top_bar_notifications import TopBarNotifications
from base.base_components.topbar_friends import TopBarFriends
from base.base_components.topbar_messages import TopBarMessages
from data.links import Links
from selenium.webdriver import Keys

from helpers.ui_helper import UIHelper

class BasePage(UIHelper):

    _MENU_LINKS_LOCATOR = "//li[contains(@class,'menu-section-links')]"
    _NEWS_FEED_LINK = "//ul[@id='menu-content']//a[contains(@class, 'newsfeed')]"
    _FRIENDS_LINK = "//ul[@id='menu-content']//a[contains(@class, 'a-friends')]"
    _PHOTOS_LINK = "//ul[@id='menu-content']//a[contains(@class, 'photos')]"
    _NOTIFICATIONS_LINK = "//ul[@id='menu-content']//a[contains(@class, 'notifications')]"
    _SEARCH_LOCATOR = "//fieldset//input[@name='q']"
    _MESSAGES_LINK = "//ul[@id='menu-content']//a[contains(@class, 'messages')]"
    _INVITE_FRIENDS_LINK = "//ul[@id='menu-content']//a[contains(@class, 'invite-friends')]"

    _NOTIFICATIONS_BUTTON_LOCATOR = "//li[@id='ossn-notif-notification']"

    def __init__(self, driver):
        super().__init__(driver)
        self.top_bar_friends = TopBarFriends(self.driver)
        self.top_bar_messages = TopBarMessages(self.driver)
        self.top_bar_notifications = TopBarNotifications(self.driver)

   # """Боковое меню"""
    @allure.step("Open/close menu link")
    def open_link_menu(self):
        self.click(self._MENU_LINKS_LOCATOR)
        self.wait_visibility_of_elements(self._NEWS_FEED_LINK)

    def click_newsfeed(self):
        self.click(self._NEWS_FEED_LINK)
        self.wait_url_to_be(Links.NEWSFEED_PAGE)

    def click_friends(self):
        self.click(self._FRIENDS_LINK)

    def click_link_notifications(self):
        self.click(self._NOTIFICATIONS_LINK)

    def search(self, name):
        search = self.find(self._SEARCH_LOCATOR)
        search.click()
        search.send_keys(name)
        search.send_keys(Keys.ENTER)

#"""Меню наверху справа"""


    def click_notification(self):
        self.click(self._NOTIFICATIONS_BUTTON_LOCATOR )

    def get_current_window_handle(self):
        window_1 = self.driver.current_window_handle
        return window_1


    def switch_to_window(self):
        self.driver.switch_to.window(self.get_current_window_handle())









