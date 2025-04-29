import pickle
import os
import platform
import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
#from faker import Faker
from data.credentials import Credentials
from libs.data_generator import Generators
from metaclasses.meta_locator import MetaLocator
from faker import Faker


class UIHelper(metaclass=MetaLocator):

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1)
        self.actions = ActionChains(self.driver)
        self.fake = Faker()
        self.credentials = Credentials()
        self.generator = Generators()

    def open(self):
        with allure.step(f"Open page: {self._PAGE_URL}"):
            self.driver.get(self._PAGE_URL)
            self.wait.until(EC.url_to_be(self._PAGE_URL))

    def is_opened(self):
        with allure.step(f"Page {self._PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self._PAGE_URL))

    @property
    def cmd_ctr_button(self):
        os_name = platform.system()
        cmd_ctr_button = Keys.COMMAND if os_name == "Darvin" else Keys.CONTROL
        return cmd_ctr_button

    def is_opened_for_user_or_admin(self, role):
        if role == "user":
            self.wait.until(EC.url_to_be(self._PAGE_URL_USER))
        elif role == "admin":
            self.wait.until(EC.url_to_be(self._PAGE_URL_Admin))



    def find(self, locator: tuple) -> WebElement:
        """
        This method helps to find element
        :param locator: Not unpacked tuple Не надо распоковывать локаторы так как мы используем явные ожидания, и там как раз идет рапаковка
        :return: WebElement
        """
        element = self.wait_for_clickable(locator)
        return element

    def find_all(self, locator: tuple) -> list[WebElement]:
        """
        This method helps to find list of all elements
        :param locator: Not unpacked tuple
        :return: WebElements list
        """
        elements = self.wait_visibility_of_elements(locator)
        return elements

    def find_last_element_of_list(self, locator: tuple) -> list[WebElement]:
        """
        This method helps to find list of all elements
        :param locator: Not unpacked tuple
        :return: WebElements list
        """
        last_element = self.wait_visibility_of_elements(locator)[-1]
        return last_element


    def click(self, locator):
        element = self.find(locator)
        element.click()

    def fill(self, locator: tuple, text: str):
        element = self.find(locator)
        element.send_keys(text)

    def clear(self, locator:tuple ):
        element = self.find(locator)
        element.clear()
        return element

    def get_text(self, locator):
        element = self.find(locator)
        element_text = element.text
        return element_text


    #скриншот для алюра
    def make_screenshot(self, name=time.time()):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=AttachmentType.PNG
        )

    # проверяем если элемент (например кнопка)есть то тогда все хорошо
    def is_element_exists(self, locator):
        try:
            self.driver.find_element()
        except:
            pass
    # --- Waits ---
    def wait_for_visibility(self, locator: tuple, message=None):
        """
        This method waits for visibility
        :param locator: Not unpacked tuple
        :return: WebElement
        """
        return self.wait.until(EC.visibility_of_element_located(locator), message=message)

    def wait_for_invisibility(self, locator: tuple, message=None):
        """
        This method waits for visibility
        :param locator: Not unpacked tuple
        :return: WebElement
        """
        return self.wait.until(EC.invisibility_of_element(locator), message=message)

    def wait_for_clickable(self, locator: tuple, message=None):
        """
        This method waits for visibility
        :param locator: Not unpacked tuple
        :return: WebElement
        """
        return self.wait.until(EC.element_to_be_clickable(locator), message=message)

    def wait_visibility_of_elements(self, locator: tuple, message=None):
        """
        This method waits for visibility
        :param locator: Not unpacked tuple
        :return: WebElement
        """
        return self.wait.until(EC.visibility_of_all_elements_located(locator), message=message)

    def wait_invisibility_of_element(self, locator: tuple, message=None):
        """
        This method waits for visibility
        :param locator: Not unpacked tuple
        :return: WebElement
        """
        return self.wait.until(EC.invisibility_of_element(locator), message=message)
    def wait_url_to_be(self, link):
        return self.wait.until(EC.url_to_be(link))

    def wait_change_text_in_element(self, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    # --- Cookies ---
    def save_cookies(self, cookies_name="temp-cookies"): #это имя  файла по умолчанию, который будет создан, куда запишутся куки, не забываем что нужно создать директрию cookies
        pickle.dump(self.driver.get_cookies(), open(f"cookies/{cookies_name}.pkl", "wb"))

    def load_cookies(self, cookies_name="temp-cookies"):
        cookies = pickle.load(open(f"cookies/{cookies_name}.pkl", "rb"))
        self.driver.delete_all_cookies()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    # --- Scrolls ---
    def scroll_by(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    def scroll_to_bottom(self):
       #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0)")

    def scroll_to_element(self, locator):
        self.actions.scroll_to_element(self.find(locator))
        self.driver.execute_script("""
        window.scrollTo({
            top: window.scrollY + 500,
        });
        """)

    def scroll_down_pixels(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

 #скролл без анимации
    def scroll_to_element1(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", element)


