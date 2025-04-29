from libs.data_generator import Generators
from pages.friends_page import FriendsPage
from pages.login_page import LoginPage
from pages.news_feed_page import NewsFeedPage
from pages.notification_page import NotificationsPage
from pages.search_page import SearchPage
from pages.user_wall_page import UserWallPage


class BaseTest:
    def setup_method(self):
        self.login_page = lambda driver=self.driver:LoginPage(driver)
        self.news_feed_page = lambda driver=self.driver: NewsFeedPage(driver)
        self.search_page = lambda driver=self.driver: SearchPage(driver)
        self.friends_page = lambda driver=self.driver: FriendsPage(driver)
        self.user_wall_page = lambda driver=self.driver: UserWallPage(driver)
        self.notifications_page = lambda driver=self.driver: NotificationsPage(driver)
        # self.messager_user_page_in_admin_account = lambda driver=self.driver: MessageUserPageInAdminAccount(driver)
        self.generator = Generators()
