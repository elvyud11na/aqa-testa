import time

import allure
import pytest

from base.base_test import BaseTest
from data.credentials import Credentials

@allure.epic("Account")
class TestFriendRequest(BaseTest):


    @pytest.mark.parametrize("add_users", [2], indirect=True)
    @allure.title("Принять дружбу администратора(через поиск юзера по имени)  - accept friendship") # полный тест
    def test_accept_friend_from_admin(self, add_users):
        admin, user = add_users
        self.login_page(admin).open()
        self.login_page(admin).is_opened()
        self.login_page(admin).login_as_admin()
        self.news_feed_page(admin).search("Lana lana")
        self.search_page(admin).click_add_friend()
        self.login_page(user).open()
        self.login_page(user).is_opened()
        self.login_page(user).login_as_user()
        self.news_feed_page(user).top_bar_friends.show_friends_request()
        self.news_feed_page(user).top_bar_friends.get_item_by_name("System Administrator")
        self.news_feed_page(user).top_bar_friends.click_confirm("System Administrator")
        time.sleep(3)