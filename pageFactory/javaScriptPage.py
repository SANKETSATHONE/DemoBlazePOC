import time

from selenium.webdriver.common.by import By
from generic.wrapperFunction import WrapperFunctions


class JavaScriptPage(WrapperFunctions):

    def __init__(self,driver):
        super().__init__(driver)

    loc_btn_alert = (By.XPATH,"//button[contains(.,'Click for JS Alert')]")
    loc_btn_click_js_confirm =(By.XPATH,"//button[contains(.,'Click for JS Confirm')]")
    loc_btn_click_js_prompt = (By.XPATH,"//button[contains(.,'Click for JS Prompt')]")

    def click_on_alert(self):
        self.click(self.loc_btn_alert)
        self.accept_alert_popup()

    def click_js_confirm(self):
        self.click(self.loc_btn_click_js_confirm)
        self.accept_alert_popup()

    def click_and_set_text_on_JS_prompt(self,key):
        self.click(self.loc_btn_click_js_prompt)
        self.set_text_alert(key)
        time.sleep(3)
        self.accept_alert_popup()









