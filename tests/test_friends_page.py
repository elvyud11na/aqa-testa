import allure
import pytest
import time

from base.base_components.topbar_friends import TopBarFriends
from base.base_test import BaseTest

@allure.epic("Friends")
class TestUserPageInAdminAccount(BaseTest):


    @pytest.mark.parametrize("add_users", [2], indirect=True)
    @allure.title("Принять дружбу администратора - accept friendship of admin") # полный тест
    def test_accept_friendship_of_admin(self, add_users):
        user, admin = add_users
        self.login_page(user).open()
        self.login_page(user).is_opened()
        self.login_page(user).login_as_user()
        self.news_feed_page(user).create_post()
        self.login_page(admin).open()
        self.login_page(admin).is_opened()
        self.login_page(admin).login_as_admin()
        self.news_feed_page(admin).click_link_name_on_post()
        self.user_wall_page(admin).is_opened_for_user_or_admin(admin)
        self.user_wall_page(admin).friend_request()
        self.news_feed_page(user).top_bar_friends.show_friends_request()
        self.news_feed_page(user).top_bar_friends.name_last_request_fried()
        self.news_feed_page(user).top_bar_friends.click_confirm_button()
        time.sleep(5)
        self.news_feed_page(user).top_bar_friends.text_after_confirm_friend()
        self.news_feed_page(user).click_friends()
        self.friends_page(user).is_opened_for_user_or_admin(user)
        self.friends_page(user).get_friend_item_by_name(f"{TopBarFriends.name_last_request_fried}")

    @allure.title("расторгнуть дружбу администратора с юзером lana")
    def test_unfriend(self):
        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as_admin()
        self.news_feed_page().click_friends()
        self.friends_page().get_list_name_users_in_friend()
        self.friends_page().get_row_content(1)
        time.sleep(5)
        #self.links_page().friends_page.click_unfriend_in_row(7)
        #self.friends_page().find_user_by_name("Lana lana")
        #self.friends_page().admin_deleting_friend("Lana lana")
        self.friends_page().admin_deleting_friend2("Lana lana")
        time.sleep(5)

    # @allure.title("расторгнуть дружбу администратора с юзером lana")
    # def test_unfriend_on_search(self):
    #     self.login_page().open()
    #     self.login_page().is_opened()
    #     self.login_page().login_us_admin()
    #     self.links_page().search("lana lana")
    #     #self.user_page_in_admin_account().unfriend()

    @allure.title("Open friends profile")
    def test_open_friends_profile(self):
        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as_admin()
        self.news_feed_page().click_friends()
        time.sleep(5)
        #self.friends_page().get_friend_item_by_name("Lana lana")
        self.friends_page().open_friends_profile("Lana")
        time.sleep(5)
