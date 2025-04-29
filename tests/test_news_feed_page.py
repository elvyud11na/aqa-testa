import allure
import pytest
import time

from base.base_test import BaseTest
from data.credentials import Credentials

@allure.epic("Account")
class TestNewFeedPage(BaseTest):

    @allure.title("Publishing a user's post")#публикация поста юзера
    def test_publishing_user_post(self):
        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as_user()
        self.news_feed_page().create_post()
        self.news_feed_page().is_post_created()

    @allure.title("User edit last post")
    def test_user_edit_last_post(self):
        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as_user()
        self.news_feed_page().user_edit_last_post("edit text")
        time.sleep(5)

    @allure.title("User edit post by text")
    def test_user_edit_post_by_text(self):
        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as_user()
        self.news_feed_page().edit_post_by_text("love", "cat")

    @allure.title("User delete post")
    def test_user_delete_post(self):
        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as_user()
        self.news_feed_page().create_post()
        time.sleep(2)
        self.news_feed_page().user_delete_self_last_post()
        time.sleep(2)


    @pytest.mark.parametrize("add_users", [2], indirect=True)
    @allure.title("User post in admin account")  # тест что пост юзера отображается в лк админа
    def test_user_post_in_admin_account(self, add_users):
        user, admin = add_users
        self.login_page(user).open()
        self.login_page(user).is_opened()
        self.login_page(user).login_as_user()
        self.news_feed_page(user).create_post()
        self.news_feed_page(user).is_post_created()
        time.sleep(5)
        self.login_page(admin).open()
        self.login_page(admin).is_opened()
        self.login_page(admin).login_as_admin()
        self.news_feed_page(admin).user_post_in_admin_account()



    @pytest.mark.parametrize("add_users", [2], indirect=True)
    @allure.title("Like user post in admin account")  # тест что админ ставит лайк посту юзера
    def test_like_user_post_in_admin_account(self, add_users):
        user, admin = add_users
        self.login_page(user).open()
        self.login_page(user).is_opened()
        self.login_page(user).login_as_user()
        self.news_feed_page(user).create_post()
        self.login_page(admin).open()
        self.login_page(admin).is_opened()
        self.login_page(admin).login_as_admin()
        self.news_feed_page(admin).admin_love_reaction_on_last_post()
        #self.news_feed_page(admin).add_emoji()
        self.news_feed_page(admin).get_love_reaction_on_user_post()

    @allure.title("Admin comment on user post")
    def test_admin_comment_on_user_post(self):
        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as_admin()
        self.news_feed_page().admin_comment_on_user_post("li")
        time.sleep(2)

    def test_create_post_2(self):
        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as_user()
        self.news_feed_page().enter_post_text()
        self.news_feed_page().click_post_button()
        time.sleep(2)
        self.news_feed_page().is_post_created()
        time.sleep(2)


    def test_open_user_wall_post_author(self):
        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as_admin()
        self.news_feed_page().click_link_name_on_post_by_name("Lana lana")
        time.sleep(3)

