import os
import allure
import pytest
from selenium import webdriver


def get_driver():
    browser = os.environ["BROWSER"]
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        options.add_argument("--disable-search-engine-choice-screen")
        options.add_argument("--window-size=1500,800")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--disable-search-engine-choice-screen")
        options.add_argument("--window-size=1500,800")
        driver = webdriver.Firefox(options=options)
    return driver

@pytest.fixture(autouse=True)
def driver(request):
    driver = get_driver()
    request.cls.driver = driver #здесь дравйвер для тестов
    yield driver  #здесь возвращаем драйвер чтобы могли использловать его в других фикстурах
    driver.quit()

@pytest.fixture()
def add_users(request): # Фикстура для добавления юзеров в тест
    user_count = request.param # Принимаем кол-во юзеров из параметров теста
    drivers = [] # Создаем пустой список драйверов, туда будем класть новых юзеров
    for _ in range(user_count):
        driver = get_driver()
        drivers.append(driver) # Тут через цикл мы добавляем новые браузеры в список
    yield drivers # Переходим к тесту
    for driver in drivers: # После теста закрываем все драйверы, которые были созданы
        driver.quit()

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)

#при падении теста делается скриншот
@pytest.fixture(autouse=True)
def take_screenshot_on_failure(request, driver):
    yield
    if request.node.rep_call.failed:   #в фикстура доступ к тесатм это request.node, в хуках это item, те.е request.node это наш тест и item тоэе наш тест
        screenshot = driver.get_screenshot_as_png() #тюе если наш тест упал, мы делаем скрин
        allure.attach(
            screenshot,
            name="Screen on failure",
            attachment_type=allure.attachment_type.PNG
        )
# #можно так вынести опции , но кажется тут надо будет что то еще подправить
# def get_options():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option('useAutomationExtension', False)
#     return options
#
# @pytest.fixture(autouse=True)
# def driver_1(request, get_options):
#     driver = webdriver.Chrome(options=get_options)
#     request.cls.driver = driver
#     yield
#     driver.quit()
#
# @pytest.fixture()
# def add_users1(request):
#     user_count = request.param  # Принимаем кол-во юзеров из параметров теста
#     drivers = []  # Создаем пустой список драйверов, туда будем класть новых юзеров
#     for _ in range(user_count):
#         driver = driver_1()
#         drivers.append(driver)  # Тут через цикл мы добавляем новые браузеры в список
#     yield drivers  # Переходим к тесту
#     for driver in drivers:  # После теста закрываем все драйверы, которые были созданы
 #       driver.quit()