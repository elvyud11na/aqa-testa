import allure
from base.base_page import BasePage
from selenium.webdriver import Keys
from data.links import Links
from selenium.webdriver.support import expected_conditions as EC
import time
from faker import Faker
fake = Faker()

class NewsFeedPage(BasePage):
    text_for_post = fake.text()
    word_for_edit_post = fake.word()

    _PAGE_URL = Links.NEWSFEED_PAGE

    _INPUT_POST_LOCATOR = "//form[@id ='ossn-wall-form']//textarea[@name='post']"
    _POST_BUTTON_LOCATOR = "//input[@value='Post']"
    _TEXT_PUBLISHED_POST_LOCATOR = ".//div[@class='post-contents']"#(Тест опубликованного поста у юзера)
    _POST_LIKE_REACTIONS_HA_HA_LOCATOR = "(//div[@class='user-activity']/div)[1]//div[contains(@class,'haha')]"
    _POST_MENU_LOCATOR = ".//div[@class='post-menu']"
    _POST_EDIT_LOCATOR = ".//a[contains(@class,'edit')]"
    _POST_EDIT_CONTENTS_INPUT_LOCATOR = "//div[@class='contents']//textarea[@id='post-edit']"
    _POST_EDIT_SAVE_BUTTON_LOCATOR = "//div[@class='ossn-message-box']//a[text()='Save']"
    _POST_EDIT_CANCEL_BUTTON_LOCATOR = "//div[@class='ossn-message-box']//a[text()='Cancel']"
    _POST_DELETE_LOCATOR = ".//a[contains(@class,'delete')]"


    ##FOR_ADMIN
    _POST_LAST_LOCATOR = "(//div[@class='user-activity']/div)[1]"
    _TEXT_ALL_POSTS = "//div[@class='post-contents']"
    _TEXT_POST_ALL = "//div[@class='post-contents']"
    _TEXT_POST_LALA_LOCATOR = "(//div[@class='post-contents'])[1]"
    _POST_LIKE_BUTTON_LOCATOR = "(//div[@class='user-activity']/div)[1]//a[@class='post-control-like']"
    _POST_LIKE_REACTIONS_BUTTON_LOCATOR = "(//div[@class='user-activity']/div)[1]//li[contains(@class,'haha')]"
    _POST_LOVE_REACTIONS_LOCATOR = "//div[@class='user-activity']//div//li[contains(@class,'love')]"
    _LOVE_REACTIONS_AFTER_REACTION = "//div[@class='like-share']//li//div[contains(@class,'like')]" #реация Love после того как поставили реакцию и она добавилась к посту
    _POST_COMMENT_BUTTON_LOCATOR = "//div[@id='activity-item-20']//a[contains(text(),'Comment')]"

    _CONFIRMATION_MESSAGE_LOCATOR = "//div[@class='ossn-system-messages-inner']//div  " #подтвеждающее сообщение например что пост исправлен или удален

    _INPUT_COMMENT_FOR_USER_POST = "//div[@class='user-activity']/div//span[@name='comment']"
    _COMMENT_IN_USER_POST_LOCATOR = "(//div[@class='user-activity']/div)[1]//span[@class='comment-text']"
    _LINK_USER_LANA_LANA_LOCATOR = "//div[@class='user']//a[text()='Lana lana']"
    _ADD_FRIEND_LANA_BUTTON_LOCATOR = "//div[@id = 'profile-menu']/a[contains(text(), 'Add Friend')]"
   #общие локаторы для всех юзеров, а не индивидуально  для Lana lana как выше
    _ALL_USER_POST = "//div[contains(@class, 'ossn-wall-item')]"
    _CANCEL_REQUEST_BUTTON_LOCATOR ="//div[@id = 'profile-menu']/a[contains(text(), 'Cancel Request')]"
    _ALL_NAME_LINK_POST_AUTHOR = "//div[@class='user']//a"
    _USER_FULL_NAME_ON_USER_WALL = "//div[@class='user-fullname']"
    _LIKE_BUTTON_LOCATOR="//div[@class='user-activity']/div//a[@class='post-control-like']"
    _LIKE_REACTIONS_LOCATOR = "//li[contains(@class,'haha')]"
    _UNLIKE_LOCATOR = "//div[@class='menu-likes-comments-share']//a[text()='Unlike']"
    _LIKE_SHARE ="//div [@class='like-share']//div[@class='ossn-reaction-list']"


    @allure.step("Enter post text")
    def enter_post_text(self):
        self.fill(self._INPUT_POST_LOCATOR, self.text_for_post)
        assert self.text_for_post == self.find(self._INPUT_POST_LOCATOR).get_attribute("value")

    @allure.step("Click post button")
    def click_post_button(self):
        self.click(self._POST_BUTTON_LOCATOR)

    @allure.step("Check post crated")
    def is_post_created(self):
        post_text_list = self.find_all(self._TEXT_POST_ALL )
        for post in post_text_list:
            if self.text_for_post in post.text:
                return True
        raise AssertionError("Post was not created")
    @allure.step("User create a post")
    def create_post(self):
        self.fill(self._INPUT_POST_LOCATOR, self.text_for_post)
        self.click(self._POST_BUTTON_LOCATOR)
        #time.sleep(2) # для проверки создания поста используем метод is_post_created()
        # text_published_post = self.get_text(self._TEXT_PUBLISHED_POST_LOCATOR)
        # assert text_published_post == self.text_for_post


    @allure.step("User edit last post")
    def user_edit_last_post(self, edit_text):
        posts = self.find_all(self._ALL_USER_POST)
        post = posts[0]
        post.find_element(*self._POST_MENU_LOCATOR).click()
        post.find_element(*self._POST_EDIT_LOCATOR).click()
        self.clear(self._POST_EDIT_CONTENTS_INPUT_LOCATOR)
        self.fill(self._POST_EDIT_CONTENTS_INPUT_LOCATOR, edit_text)
        assert self.find(self._POST_EDIT_CONTENTS_INPUT_LOCATOR).get_attribute("value") == edit_text
        self.click(self._POST_EDIT_SAVE_BUTTON_LOCATOR)
        assert self.find(self._CONFIRMATION_MESSAGE_LOCATOR).is_displayed() is True, "no message"
        assert self.get_text(self._CONFIRMATION_MESSAGE_LOCATOR) == "Post successfully saved"
        self.wait_for_invisibility(self._CONFIRMATION_MESSAGE_LOCATOR)


    def edit_post_by_text(self, text, edit_text):
        posts = self.find_all(self._ALL_USER_POST)
        for post in posts:
            if text in post.text:
                post.find_element(*self._POST_MENU_LOCATOR).click()
                post.find_element(*self._POST_EDIT_LOCATOR).click()
                self.clear(self._POST_EDIT_CONTENTS_INPUT_LOCATOR)
                self.fill(self._POST_EDIT_CONTENTS_INPUT_LOCATOR, edit_text)
                assert self.find(self._POST_EDIT_CONTENTS_INPUT_LOCATOR).get_attribute("value") == edit_text
                self.click(self._POST_EDIT_SAVE_BUTTON_LOCATOR)
                assert self.find(self._CONFIRMATION_MESSAGE_LOCATOR).is_displayed() is True, "no message"
                assert self.get_text(self._CONFIRMATION_MESSAGE_LOCATOR) == "Post successfully saved"
                self.wait_for_invisibility(self._CONFIRMATION_MESSAGE_LOCATOR)
                break


    @allure.step("Add emoji in post")
    # TOODO придумать провеку
    def add_emoji(self):
        posts = self.find_all(self._TEXT_ALL_POSTS)
        last_past = posts[0]
        last_past.find_element(*self._LIKE_BUTTON_LOCATOR).click()
        emoji = last_past.find_elements(*self._LIKE_REACTIONS_LOCATOR)
        selected_emoji = emoji[self.generator.generate_number(0, len(emoji)-1)]
        selected_emoji.click()
        #assert selected_emoji.text in self.find(self._INPUT_POST_LOCATOR).get_attribute("value")


    @allure.step("User delete self last post")
    def user_delete_self_last_post(self):
        posts = self.find_all(self._ALL_USER_POST)
        post = posts[0]
        content_post = post.find_element(*self._TEXT_PUBLISHED_POST_LOCATOR).text# текст последнего поста
        post.find_element(*self._POST_MENU_LOCATOR).click()
        post.find_element(*self._POST_DELETE_LOCATOR).click()
        posts = self.find_all(self._ALL_USER_POST)
        post = posts[0]
        content_post_after = post.find_element(*self._TEXT_PUBLISHED_POST_LOCATOR).text# текст последнего поста после удаления
        assert content_post != content_post_after, "последний ост не удалился или возможно два последних поста одинаковые"


    @allure.step("User post in admin account")
    def user_post_in_admin_account(self):
        post_user = self.wait_for_visibility(self._TEXT_POST_LALA_LOCATOR)
        post_user_text = post_user.text
        assert self.text_for_post == post_user_text

    @allure.step("Admin love reaction on user post")
    def admin_love_reaction_on_last_post(self):
        posts = self.find_all(self._TEXT_ALL_POSTS)
        last_past = posts[0]
        last_past.find_element(*self._LIKE_BUTTON_LOCATOR).click()
        last_past.find_element(*self._POST_LOVE_REACTIONS_LOCATOR).click()
        # self.wait_for_visibility(self._POST_LAST_LOCATOR)
        # self.click(self._POST_LIKE_BUTTON_LOCATOR)
        # self.click(self._POST_LIKE_REACTIONS_BUTTON_LOCATOR)
        # time.sleep(2)

    @allure.step("Get love reaction on user post")
    def get_love_reaction_on_user_post(self):
        self.driver.refresh()
        posts = self.find_all(self._TEXT_ALL_POSTS)
        last_past = posts[0]
        self.wait_for_visibility(self._LOVE_REACTIONS_AFTER_REACTION)
        love = last_past.find_element(*self._LOVE_REACTIONS_AFTER_REACTION)
        print(love)

    @allure.step("Admin comment on user post")
    def admin_comment_on_user_post(self, text):
        posts = self.find_all(self._TEXT_ALL_POSTS)
        last_past = posts[0]
        comment = last_past.find_element(*self._INPUT_COMMENT_FOR_USER_POST)
        comment.click()
        comment.send_keys(text, Keys.ENTER)
        time.sleep(1)
        self.wait_visibility_of_elements(self._COMMENT_IN_USER_POST_LOCATOR)
        last_comment_after = self.find_all(self._COMMENT_IN_USER_POST_LOCATOR)
        last_comment_after = last_comment_after[-1].text
        assert text == last_comment_after, "коммент не добавился"


    @allure.step("Admin click on name of post(Lana lana)")
    def click_link_name_on_post(self):
        self.click(self._LINK_USER_LANA_LANA_LOCATOR)
        self.wait_for_visibility(self._USER_FULL_NAME_ON_USER_WALL)
        assert self.driver.current_url == "https://demo.opensource-socialnetwork.org/u/GarryPotter"


    def click_link_name_on_post_by_name(self, name):
        with allure.step(f"Admin click on name link of post author's: '{name}'"):
            all_name_link = self.find_all(self._ALL_NAME_LINK_POST_AUTHOR)
            for name_link in all_name_link:
                if name_link.text == name:
                    name_link.click()
                    self.wait_for_visibility(self._USER_FULL_NAME_ON_USER_WALL)
                    assert self.get_text(self._USER_FULL_NAME_ON_USER_WALL) == name
                    break
                else:
                    raise AssertionError("Такой юзер еще не опубликовал пост")



    # @allure.step("Admin send friend request user Lana lana")
    # def friend_request(self):
    #     self.click(self._LINK_USER_LANA_LANA_LOCATOR)
    #     time.sleep(5)
    #     assert self.driver.current_url == "https://demo.opensource-socialnetwork.org/u/GarryPotter"
    #     self.click(self._ADD_FRIEND_LANA_BUTTON_LOCATOR)
    #     self.wait_change_text_in_element(self._CANCEL_REQUEST_BUTTON_LOCATOR,"Cancel Request")
    #     self.wait_for_clickable(self._CANCEL_REQUEST_BUTTON_LOCATOR)









#<div class="alert alert-dismissible alert-success"><button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>Post successfully saved</div>
