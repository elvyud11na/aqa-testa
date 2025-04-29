import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

from base.base_page import BasePage
from data.links import Links
import time

class FriendsPage(BasePage):

    _PAGE_URL = Links.FRIENDS_PAGE
    _PAGE_URL_USER = Links.FRIENDS_PAGE_USER
    _PAGE_URL_ADMIN = Links.FRIENDS_PAGE_ADMIN


    _FRIEND_NAME_LOCATOR = "//div[@class='module-contents']//a[contains(@class,'user')]"
    # _TEXT_AFTER_CONFIRM_FRIENDS = "//div[@class='notfi-meta']//div"
    # _TEXT_AFTER_UNFRIEND_LOCATOR = "//div[@class='ossn-system-messages-inner']"
    #
    # def click_link_user(self):
    # def name_new_friend(self):
    #     name = self.get_text(self._FRIEND_NAME_LOCATOR)
    #     assert name == "System Administrator"


    _FRIENDS_TABLE = "//div[@class ='module-contents']"
    _FRIENDS_ITEMS = ".//div[@class='row ossn-users-list-item']"
    _ITEM_FRIENDS_NAME = ".//div[class='uinfo']//a"
    _CELLS_LOCATOR = ".//div[contains(@class,'col')]"
    _NAME_FRIEND_LOCATOR = ".//a[contains(@class,'userlink')]"
    _TEXT_AFTER_UNFRIEND = "//div[contains(@class,'alert-dismissible')]"
    _UNFRIEND_BUTTON_LOCATOR = ".//a[text()='Unfriend']"
    _NEXT_PAGE_BUTTON_LOCATOR = "//ul[contains(@class,'pagination')]//a[text()='Last']"
    _FOOTER_ABOUT_LOCATOR = "//div[@class='ossn-footer-menu']/a[@class='menu-footer-about']"
    _SEARCH_LOCATOR = "//fieldset//input[@name='q']"
    @property
    def _friends_table(self):
        return self.driver.find_element(*self._FRIENDS_TABLE)

    @property
    def _rows(self) -> list[WebElement]:  #'это ряды таблицы
        friends_table = self._friends_table
        return friends_table.find_elements(*self._FRIENDS_ITEMS)


    @property
    def cell(self):
        friends_table = self._friends_table
        return friends_table.find_elements(*self._CELLS_LOCATOR)

    @allure.step("Get row content by number row")
    def get_row_content(self, row_number):
        row = self._rows[row_number - 1]
        content = []
        for cell in row.find_elements(*self._CELLS_LOCATOR):
            content.append(cell.text)
        print(content)
        #return [cell.text for cell in row.find_elements(*self._CELLS_LOCATOR)]

    @allure.step("Расторгнуть дружбу с юзером который находится  в заданной строке")
    def click_unfriend_in_row(self, row_number):
        row = self._rows[row_number - 1]
        row.find_element(*self._UNFRIEND_BUTTON_LOCATOR).click()


    @allure.step("Get  list name users in friend")
    def get_list_name_users_in_friend(self):
        column_content = []
        for row in self._rows:
            cells = row.find_elements(*self._CELLS_LOCATOR)
            column_content.append(cells[1].text)
        print(column_content)

    @allure.step("Find user by name")
    def find_user_by_name(self, text):
        for row in self._rows:
            cells = row.find_elements(*self._CELLS_LOCATOR)
            cell_text = cells[1].text
            if text in cell_text:
                print("OK")


    @allure.step("Admin deleting friend by name")
    def admin_deleting_friend(self, text):
        for row in self._rows:
            cells = row.find_elements(*self._CELLS_LOCATOR)
            cell_text = cells[1].text
            if text in cell_text:
                print("OK")
                row.find_element(*self._UNFRIEND_BUTTON_LOCATOR).click()
                return True
            else:
                raise AssertionError("Такого юзера нет в друзьях у админа, добавьте его в друзья")

    def next_page(self):
        next_button = self.find(self._NEXT_PAGE_BUTTON_LOCATOR)
        return next_button

    def get_friend_item_by_name(self, friend_name: str):
        while True:
            list_friends = self._rows
            for friend_item in list_friends:
                user_link = friend_item.find_element(*self._NAME_FRIEND_LOCATOR)
                if friend_name in user_link.text:
                    return user_link
            next_page_button = self.find(self._NEXT_PAGE_BUTTON_LOCATOR)
            self.scroll_to_element1(next_page_button)
            next_page_button.click()

    def open_friends_profile(self, friend_name: str):
        with allure.step(f"Open Friend's Profile: '{friend_name}'"):
            user_link = self.get_friend_item_by_name(friend_name)
            self.scroll_to_element1(user_link)
            user_link.click()
            # if user_link:
            #     self.scroll_to_element1(user_link)
            #     user_link.click()
            # else:
            #     raise AssertionError(f"Не удалось найти профиль друга с именем {friend_name}.")

    def get_button_unfriend_for_friend_by_name(self, friend_name: str):
        while True:
            list_friends = self._rows
            for friend_item in list_friends:
                user_link = friend_item.find_element(*self._NAME_FRIEND_LOCATOR)
                unfriend = friend_item.find_element(*self._UNFRIEND_BUTTON_LOCATOR)
                if friend_name in user_link.text:
                    return unfriend
            next_page_button = self.find(self._NEXT_PAGE_BUTTON_LOCATOR)
            self.scroll_to_element1(next_page_button)
            next_page_button.click()

    def admin_deleting_friend2(self, friend_name: str):
        with allure.step(f"Open Friend's Profile: '{friend_name}'"):
            user_unfriend = self.get_button_unfriend_for_friend_by_name(friend_name)
            self.scroll_to_element1(user_unfriend)
            user_unfriend.click()
            assert self.get_text(self._TEXT_AFTER_UNFRIEND) == "Friend request deleted!"



#        //div[contains(@class,'alert-dismissible')]     "<div class="alert alert-dismissible alert-danger">
# Friend request deleted!<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
# </div>"
    #  """тоже рабочий код"""
    # def open_friends_profile(self, friend_name):
    #     list_friends = self._rows
    #     for row in list_friends:
    #         cells = row.find_elements(*self._CELLS_LOCATOR)
    #         cell_text = cells[1].text
    #         if friend_name in cell_text:
    #             print("OK")
    #             row.find_element(*self._NAME_FRIEND_LOCATOR).click()
    #             return True

    # def next_page(self):
        #next_button = self.find(self._NEXT_PAGE_BUTTON_LOCATOR)
        #        return next_button

        # next_button = self.find(self._NEXT_PAGE_BUTTON_LOCATOR)
        # if next_button.is_displayed():
        #     next_button.click()
        # else:
        #     raise AssertionError(f"Кнопка следующей страницы недоступна или не отображается.")

    # def check_text_in_column(self, column_name, text_to_find):
    #     rows = self._rows
    #     # Проходимся по всем строкам и ищем текст в нужной колонке
    #     for row in rows:
    #         cells = row.find_elements(*self._CELLS_LOCATOR)
    #         unfriend = row.find_element(*self._UNFRIEND_BUTTON_LOCATOR)
    #         cell_text = cells[column_name - 1].text
    #         if text_to_find in cell_text:
    #             print(unfriend)
    #             unfriend.click()
    #             time.sleep(5)
    # Если текст не найден, вызываем метод click_next_page
    #     else:
    #         self.click_next_page()
    # return self.check_text_in_column(column_name, text_to_find)

    # def get_friend_by_name(self, friend_name):
    #     while True:
    #         next_page_button = self.find(self._NEXT_PAGE_BUTTON_LOCATOR)
    #         self.scroll_to_element1(next_page_button)
    #         self.wait_for_clickable(self._NEXT_PAGE_BUTTON_LOCATOR)
    #         list_friends = self._rows
    #         for friend_item in list_friends:
    #             item = friend_item.find_element(*self._NAME_FRIEND_LOCATOR)
    #             if friend_name in item.text:
    #                 return friend_item
    #         self.next_page().click()
    #
    # def open_friends_profile(self, friend_name: str):
    #     with allure.step(f"Open Friend's Profile: '{friend_name}'"):
    #         user_link = self.get_friend_by_name(friend_name)
    #         self.scroll_to_element(user_link)
    #         user_link.click()
    #
