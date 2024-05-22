import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WrapperFunctions:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        try:
            ele = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
            self.set_highlighter(ele)
            ele.click()
        except Exception:
            print("click error intercepted")

    def setText(self, locator, textValue):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).clear()
            ele = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            self.set_highlighter(ele)
            ele.send_keys(textValue)
        except Exception:
            print("set text exception")

    def getText(self, locator):
        try:
            webelement = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            return webelement.text
        except Exception as error:
            print(error)

    def get_text_from_alert(self):
        try:
            time.sleep(2)
            alert_message = Alert(driver=self.driver)
            return alert_message.text
        except Exception as error:
            print(error)

    def verify_alert_text(self, text):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            if text == self.get_text_from_alert():
                return True
        except Exception as error:
            return "alert is not present"

    def accept_alert_popup(self):
        try:
            Alert(self.driver).accept()
        except Exception as error:
            print(error)

    def is_element_enabled(self, locator):
        try:
            webelement = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            self.set_highlighter(webelement)
            return bool(webelement)
        except Exception as error:
            print(error)

    def getTitle(self, title):
        try:
            WebDriverWait(self.driver, 10).until(EC.title_is(title))
            return self.driver.title
        except Exception as error:
            print(error)

    def is_element_visible(self, locator):
        try:
            webelement = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            self.set_highlighter(webelement)
        except Exception as error:
            print("erro", error)

    def set_implicit_wait(self, wait_time):
        self.driver.implicitlywait(wait_time)

    def clearText(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).clear()
        except Exception as error:
            print(error)

    def waitFor(self, timeDuration):
        time.sleep(timeDuration)

    def move_to_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
        except Exception as error:
            print("error move to element-->", error)

    def select_dropdown(self, locator, drpOption):
        try:
            self.driver.find_element(locator).click()
            options = Select(self.driver.find_element(locator))
            options.select_by_visible_text(drpOption)
        except Exception as ex:
            print("Exception : ", ex)

    def get_element_list(self, locator):
        element_list = []
        try:
            web_elements = self.driver.find_elements(locator)
            for i in web_elements:
                element_list.append(i.text)
                return element_list
        except Exception as exp:
            print(exp)

    def set_highlighter(self, element):
        self.driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');",
                                   element)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element)
