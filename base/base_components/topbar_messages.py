import allure
from data.links import Links
from helpers.ui_helper import UIHelper
from metaclasses.meta_locator import MetaLocator



class TopBarMessages(UIHelper, metaclass=MetaLocator):
    MESSAGES_ALL = Links.MESSAGES_ALL

    _MESSAGES_BUTTON_LOCATOR = "//li[@id='ossn-notif-messages']"
    _SEE_ALL_BUTTON = "//div[@class='bottom-all']//a"
    _ALL_NAME_SEND_MESSAGES = "//div[@class='user-item-inner']//div[@class='name']"

    @allure.step("Open messages")
    def open_messages(self):
        self.click(self._MESSAGES_BUTTON_LOCATOR)
    def name_send_last_massages(self):
        last_name = self.find_all(self._ALL_NAME_SEND_MESSAGES)[-1]
        print(last_name.text)


    def show_all_messages(self):
        self.click(self._SEE_ALL_BUTTON)
        assert self.driver.current_url == self.MESSAGES_ALL