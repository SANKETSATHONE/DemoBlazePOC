import logging
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generic.testUtil import TestUtil


class WrapperFunctions:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        try:
            ele = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
            self.set_highlighter(ele)
            ele.click()
            TestUtil.logger.log(logging.INFO, f"user is able to  click on xpath {locator[1]} ")
        except Exception:
            TestUtil.logger.log(logging.INFO, "click error intercepted")

    def setText(self, locator, textValue):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).clear()
            ele = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            self.set_highlighter(ele)
            ele.send_keys(textValue)
            TestUtil.logger.log(logging.INFO, f"user is able to enter text in xpath {locator[1]} ")
        except Exception:
            TestUtil.logger.log(logging.INFO, "set text exception")

    def getText(self, locator):
        try:
            webelement = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            TestUtil.logger.log(logging.INFO, f"user is able to get text from xpath {locator[1]}")
            return webelement.text
        except Exception as error:
            TestUtil.logger.log(logging.INFO, error)

    def get_text_from_alert(self):
        try:
            time.sleep(2)
            alert_message = Alert(driver=self.driver)
            TestUtil.logger.log(logging.INFO, f"user is able to get text {alert_message.text} from alert")
            return alert_message.text
        except Exception as error:
            TestUtil.logger.log(logging.INFO, error)

    def set_text_alert(self, key):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            TestUtil.logger.log(logging.INFO, f"user is able to set text {key} in alert")
            return alert.send_keys(key)
        except Exception as error:
            TestUtil.logger.log(logging.INFO, error)

    def verify_alert_text(self, text):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            if text == self.get_text_from_alert():
                TestUtil.logger.log(logging.INFO, f"user is abe to verify text {text} form alert")
                return True
        except Exception as error:
            return "alert is not present"

    def accept_alert_popup(self):
        try:
            Alert(self.driver).accept()
            TestUtil.logger.log(logging.INFO, "User is able to accept alert popup")
        except Exception as error:
            TestUtil.logger.log(logging.INFO, error)

    def is_element_enabled(self, locator):
        try:
            webelement = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            self.set_highlighter(webelement)
            TestUtil.logger.log(logging.INFO, f"element with xpath {locator[1]} is enabled")
            return bool(webelement)
        except Exception as error:
            TestUtil.logger.log(logging.INFO, error)

    def getTitle(self, title):
        try:
            WebDriverWait(self.driver, 10).until(EC.title_is(title))
            return self.driver.title
        except Exception as error:
            TestUtil.logger.log(logging.INFO, error)

    def is_element_visible(self, locator):
        try:
            webelement = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            self.set_highlighter(webelement)
            TestUtil.logger.log(logging.INFO, f"user ia able to see the element on DOM with xpath {locator[1]}")
        except Exception as error:
            TestUtil.logger.log(logging.INFO, "erro", error)

    def set_implicit_wait(self, wait_time):
        self.driver.implicitlywait(wait_time)

    def clearText(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).clear()
        except Exception as error:
            TestUtil.logger.log(logging.INFO, error)

    def waitFor(self, timeDuration):
        time.sleep(timeDuration)

    def move_to_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            TestUtil.logger.log(logging.INFO, f"user is able to move to element having xpath {locator[1]}")
        except Exception as error:
            TestUtil.logger.log(logging.INFO, "error move to element-->", error)

    def select_dropdown(self, locator, drpOption):
        try:
            self.driver.find_element(locator).click()
            options = Select(self.driver.find_element(locator))
            options.select_by_visible_text(drpOption)
        except Exception as ex:
            TestUtil.logger.log(logging.INFO, "Exception : ", ex)

    def get_element_list(self, locator):
        element_list = []
        try:
            web_elements = self.driver.find_elements(locator)
            for i in web_elements:
                element_list.append(i.text)
                return element_list
        except Exception as exp:
            TestUtil.logger.log(logging.INFO, exp)

    def set_highlighter(self, element):
        self.driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');",
                                   element)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element)
