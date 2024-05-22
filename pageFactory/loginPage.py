import time
import allure
from selenium.webdriver.common.by import By
from generic.wrapperFunction import WrapperFunctions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(WrapperFunctions):

    def __init__(self, driver):
        super().__init__(driver)

    loc_inp_username = (By.XPATH, "//input[@id='loginusername']")
    loc_inp_password = (By.XPATH, "//input[@id='loginpassword']")
    loc_btn_login = (By.XPATH, "//button[normalize-space()='Log in']")
    loc_btn_close = (By.XPATH, "//div[@id='logInModal']//button[@type='button'][normalize-space()='Close']")

    @allure.step("enter username to login popup page")
    def enter_username(self, username):
        self.setText(self.loc_inp_username, username)

    @allure.step("enter password to login popup page")
    def enter_password(self, password):
        self.setText(self.loc_inp_password, password)

    @allure.step("click on login")
    def click_login(self, username):
        self.click(self.loc_btn_login)
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            self.verify_alert_text("Wrong password.")
            self.accept_alert_popup()
            self.click(self.loc_btn_close)
        except Exception:
            time.sleep(5)
            self.is_element_visible((By.XPATH, f"//a[contains(.,'{username}')]"))


