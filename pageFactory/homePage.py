import time
from generic.fileFunctionUtil import FileFunctionUtil as FU
from selenium.webdriver.common.by import By
from generic.wrapperFunction import WrapperFunctions
import allure


class HomePage(WrapperFunctions):

    def __init__(self, driver):
        super().__init__(driver)

    loc_p_copyright = (By.XPATH, "//p[contains(.,'Copyright © Product Store 2017')]")
    loc_btn_next = (By.XPATH, "//button[@id='next2']")
    loc_div_last_prod = (By.XPATH, "//div[@id='tbodyid']/div[last()]/div/div/h4/a")
    loc_a_add_to_cart = (By.XPATH, "//a[normalize-space()='Add to cart']")
    loc_btn_place_order = (By.XPATH, "//button[normalize-space()='Place Order']")
    loc_inp_name = (By.XPATH, "//input[@id='name']")
    loc_inp_country = (By.XPATH, "//input[@id='country']")
    loc_inp_city = (By.XPATH, "//input[@id='city']")
    loc_inp_credit = (By.XPATH, "//input[@id='card']")
    loc_inp_month = (By.XPATH, "//input[@id='month']")
    loc_inp_year = (By.XPATH, "//input[@id='year']")
    loc_btn_purchase = (By.XPATH, "//button[normalize-space()='Purchase']")
    loc_h2_verification = (By.XPATH, "//h2[contains(.,'Thank you for your purchase')]")
    loc_btn_accept_purchase = (By.XPATH, "//button[normalize-space()='OK']")
    loc_a_login = (By.XPATH, "//a[@id='login2']")

    @allure.step("user click on navigation menu")
    def click_on_navigation_menu(self, navigation_option):
        self.is_element_visible((By.XPATH, f"//a[contains(.,'{navigation_option}')]"))
        self.click((By.XPATH, f"//a[contains(.,'{navigation_option}')]"))

    @allure.step("select category")
    def select_category(self, category):
        self.click((By.XPATH, f"//a[contains(.,'{category}')]"))

    @allure.step("verify products are visible")
    def verify_products_are_visible(self, *args):
        self.driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(1)
        for product in args:
            self.is_element_visible((By.XPATH, f"//a[contains(.,'{product}')]"))

    @allure.step("scroll to bottom")
    def scroll_to_bottom(self):
        self.move_to_element(self.loc_p_copyright)

    @allure.step("click on next")
    def click_on_next(self):
        self.click(self.loc_btn_next)

    @allure.step("click on last_product")
    def click_on_last_product(self):
        time.sleep(3)
        text = self.getText(self.loc_div_last_prod)
        self.click(self.loc_div_last_prod)
        return text

    @allure.step("add product to cart")
    def add_product_to_cart(self):
        self.click(self.loc_a_add_to_cart)
        time.sleep(1)
        alert_text = self.get_text_from_alert()
        if alert_text == "Product added.":
            self.accept_alert_popup()

    @allure.step("verify added product")
    def verify_added_product(self, product):
        time.sleep(3)
        self.is_element_visible((By.XPATH, f"//tbody[@id='tbodyid']/tr/td[contains(.,'{product}')]"))

    @allure.step("place order")
    def place_order(self):
        self.click(self.loc_btn_place_order)

    @allure.step("enter name")
    def enter_name(self, name):
        self.setText(self.loc_inp_name, name + f"{FU.get_random_string(3)}")

    @allure.step("enter country")
    def enter_country(self, country):
        self.setText(self.loc_inp_country, country + f"{FU.get_random_string(3)}")

    @allure.step("enter city")
    def enter_city(self, city):
        self.setText(self.loc_inp_city, city + f"{FU.get_random_string(3)}")

    @allure.step("enter credit card details")
    def enter_credit_card_details(self):
        self.setText(self.loc_inp_credit, FU.get_random_number(12))

    @allure.step("enter month")
    def enter_month(self, month):
        self.setText(self.loc_inp_month, month)

    @allure.step("enter year")
    def enter_year(self, year):
        self.setText(self.loc_inp_year, year)

    @allure.step("click on purchase")
    def click_purchase(self):
        self.click(self.loc_btn_purchase)

    @allure.step("verify purchase")
    def verify_purchase(self, true):
        if true:
            self.is_element_visible(self.loc_h2_verification)
        else:
            self.is_element_visible(self.loc_h2_verification)
            raise Exception("product is not added to cart but purchase message popped up.. !!!")

    @allure.step("accept purchase")
    def accept_purchase(self):
        self.click(self.loc_btn_accept_purchase)

    @allure.step("verify successful logout")
    def verify_successful_logout(self):
        self.is_element_visible(self.loc_a_login)
