import allure

from data.links import Links
from helpers.ui_helper import UIHelper
from metaclasses.meta_locator import MetaLocator


class TopBarNotifications(UIHelper, metaclass=MetaLocator):
    _NOTIFICATIONS_LOCATOR = "//div[contains(@class,'icons-topbar-notifications')]"
    _NOTIFICATIONS_DROPDOWN = "//div[@ id='notificationBox']"
    _ALL_NOTIFICATIONS_LOCATOR ="//div[@class='ossn-notifications-all']//div[@class='data']"
    _SEE_ALL = "//div[@class='bottom-all']/a"




    @allure.step("Open notifications dropdown")
    def open_notifications_dropdown(self):
        self.click(self._NOTIFICATIONS_LOCATOR)
        assert self.wait_for_visibility(self._NOTIFICATIONS_DROPDOWN)

    @allure.step("Text notification on liked post")
    def text_notification_on_liked_post(self):
        text = self.get_text(self._ALL_NOTIFICATIONS_LOCATOR)
        assert "liked your post" in text

    @allure.step("Text notification on comment post")
    def text_notification_on_commented_post(self):
        text = self.get_text(self._ALL_NOTIFICATIONS_LOCATOR)
        assert "commented on the post" in text

    def see_all_notification(self):
        self.click(self._SEE_ALL)
        assert self.driver.current_url == Links.NOTIFICATIONS_PAGE

