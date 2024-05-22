import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrOptions
from selenium.webdriver.firefox.options import Options as fireOptions
import datetime
from generic.propertyManager import ReadconfigProperty



@pytest.fixture()
def setup():
    browser = ReadconfigProperty.get_config_data("browser")
    global web_driver
    web_driver = None
    if browser.lower() == "chrome":
        chrome_options = chrOptions()
        chrome_options.add_argument("'--disable-blink-features=AutomationControlled'")
        web_driver = webdriver.Chrome(options=chrome_options)
    elif browser.lower() == "firefox":
        options = fireOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        web_driver = webdriver.Firefox(options=options)
    elif browser.lower() == "edge":
        web_driver = webdriver.Edge()
    web_driver.implicitly_wait(ReadconfigProperty.get_config_data("wait.implicit"))
    web_driver.maximize_window()
    baseurl = ReadconfigProperty.get_config_data('baseurl')
    web_driver.get(baseurl)
    return web_driver


@pytest.fixture()
def timeStamp():
    current_time = datetime.datetime.now()
    print("\n Execution Start at", current_time)
    yield
    print("\nExecution ends at", current_time)


@pytest.fixture()
def teardown():
    yield
    web_driver.quit()


