import allure
from base.base_page import BasePage
from data.links import Links

class NotificationsPage(BasePage):

    _PAGE_URL = Links.NOTIFICATIONS_PAGE

    _ALL_NOTIFICATIONS = "//div[contains(@class,'ossn-notification-page')]/a"

#TOODO придумать проверку
    def open_post_with_notifications(self, nimber_notificatio):
        notifications = self.find_all(self._ALL_NOTIFICATIONS)
        last_notification = notifications[nimber_notificatio-1]
        last_notification.click()
        #assert