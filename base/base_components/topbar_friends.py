import allure


from helpers.ui_helper import UIHelper
from metaclasses.meta_locator import MetaLocator


class TopBarFriends(UIHelper, metaclass=MetaLocator):

    name_last_request_fried = ""

    _FRIEND_REQUEST_LOCATOR = "//li[@id='ossn-notif-friends']"
    _CONFIRM_BUTTON_LOCATOR = "//input[@value='Confirm']"
    _DENY_BUTTON_LOCATOR = "//input[@value='Deny']"
    _NAME_FRIEND_REQUEST_LOCATOR = "//div[@class='notfi-meta']//a"  #имя кто предлагает дружбу
    _TEXT_AFTER_CONFIRM_FRIENDS_LOCATOR = "//div[@class='notfi-meta']//div"
    _TEXT_AFTER_DENY_FRIENDS_LOCATOR = "//div[@class='notfi-meta']//div"
    _REQUEST_LIST = "//div[@class='notification-friends']"
    _ITEM_TEXT = ".//a"
    _ITEM_CONFIRM_BUTTON = ".//input[@value='Confirm']"



    @allure.step("Shou friends request")
    def show_friends_request(self):
        self.click(self._FRIEND_REQUEST_LOCATOR)

    @allure.step("Confirm friend")
    def click_confirm_button(self):
        self.click(self._CONFIRM_BUTTON_LOCATOR)

    @allure.step("Deny friend")
    def click_deny_friend(self):
        self.click(self._DENY_BUTTON_LOCATOR)

    @allure.step("Name of the last person who offered friendship") #Name of the last person who offered friendship
    def name_last_request_fried(self):
        TopBarFriends.name_last_request_fried = self.find_all(self._NAME_FRIEND_REQUEST_LOCATOR)[-1].text
        return TopBarFriends.name_last_request_fried

    @allure.step("Notification after confirm friend")
    def text_after_confirm_friend(self):
        text = self.get_text(self._TEXT_AFTER_CONFIRM_FRIENDS_LOCATOR)
        assert text == "You are now friends!"

    @allure.step("Notification after deny friend")
    def text_after_deny_friend(self):
        text = self.get_text(self._TEXT_AFTER_DENY_FRIENDS_LOCATOR)
        assert text == "Friend request deleted!"

    @property
    def _request_items(self):
        return self.find_all(self._REQUEST_LIST)

#"""Проверяем по имени есть ли в списке тот кто предложил дружбу"""
    def get_item_by_name(self, friend_name:str):
        for request_item in self._request_items:
            item = request_item.find_element(*self._ITEM_TEXT)
            if friend_name == item.text:
                return request_item
        raise AssertionError(f"Request from '{friend_name}' was not found")

    def is_friend_request_got(self,friend_name):
        with allure.step(f"Check Received a Friend Request from '{friend_name}'"):
            if self.get_item_by_name(friend_name):
                return True
            raise AssertionError("Request was not received ")

    @allure.step("Click Confirm button")
    def click_confirm(self, friend_name):
        request_item = self.get_item_by_name(friend_name)
        confirm_button = request_item.find_element(*self._ITEM_CONFIRM_BUTTON)
        self.click(confirm_button)
        self.wait_invisibility_of_element(confirm_button, message="The button Confirm was not ///")


