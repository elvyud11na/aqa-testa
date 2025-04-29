import allure
import pytest
import time

from base.base_test import BaseTest
from data.credentials import Credentials

@allure.epic("Account")
class TestNotifications(BaseTest):

    @pytest.mark.parametrize("add_users", [2], indirect=True)
    @allure.title("Notification liked post")
    def test_notification_liked_post(self, add_users):  # проверяем что приходит уведомление когда лайкнули пост
        user, admin = add_users
        self.login_page(user).open()
        self.login_page(user).is_opened()
        self.login_page(user).login_as_user()
        self.news_feed_page(user).create_post()
        self.login_page(admin).open()
        self.login_page(admin).is_opened()
        self.login_page(admin).login_as_admin()
        self.news_feed_page(admin).admin_love_reaction_on_last_post()
        self.news_feed_page(user).top_bar_notifications.open_notifications_dropdown()
        self.news_feed_page(user).top_bar_notifications.text_notification_on_liked_post()

    @pytest.mark.parametrize("add_users", [2], indirect=True)
    @allure.title("Notification comment post")
    def test_notification_comment_post(self,
                                       add_users):  # проверяем что приходит уведомление когда оставили коммент к пост
        user, admin = add_users
        self.login_page(user).open()
        self.login_page(user).is_opened()
        self.login_page(user).login_as_user()
        self.news_feed_page(user).create_post()
        self.login_page(admin).open()
        self.login_page(admin).is_opened()
        self.login_page(admin).login_as_admin()
        self.news_feed_page(admin).admin_comment_on_user_post("ay")
        self.news_feed_page(user).top_bar_notifications.open_notifications_dropdown()
        self.news_feed_page(user).top_bar_notifications.text_notification_on_commented_post()

    def test_open_post_last_notification(self):
        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as_user()
        self.news_feed_page().click_link_notifications()
        self.notifications_page().is_opened()
        self.notifications_page().open_post_with_notifications(10)
