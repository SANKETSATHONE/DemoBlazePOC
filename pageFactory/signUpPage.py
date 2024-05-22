import allure

from selenium.webdriver.common.by import By
from generic.wrapperFunction import WrapperFunctions


class SignUpPage(WrapperFunctions):

    def __init__(self, driver):
        super().__init__(driver)

    loc_inp_username = (By.XPATH, "//input[@id='sign-username']")
    loc_inp_password = (By.XPATH, "//input[@id='sign-password']")
    loc_btn_signup = (By.XPATH, "//button[normalize-space()='Sign up']")

    @allure.step("enter username in sign up popup page")
    def enter_username(self, username):
        self.setText(self.loc_inp_username, username)

    @allure.step("enter password in sign up popup page")
    def enter_password(self, password):
        self.setText(self.loc_inp_password, password)

    @allure.step("click on sign up")
    def click_sign_up(self):
        self.click(self.loc_btn_signup)

    @allure.step("verify new user gets sign in")
    def verify_new_user_signup(self):
        if self.verify_alert_text("Sign up successful."):
            self.accept_alert_popup()
            return "user successfully singed up"
        elif self.verify_alert_text("This user already exist."):
            self.accept_alert_popup()
            return "user signup failed this user already exist"


