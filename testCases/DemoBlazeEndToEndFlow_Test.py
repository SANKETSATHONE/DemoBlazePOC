import time
from generic.fileFunctionUtil import FileFunctionUtil as FU
import pytest
from pageFactory.homePage import HomePage
from pageFactory.loginPage import LoginPage
from pageFactory.signUpPage import SignUpPage
from generic.ExcelUtil import ExcelUtil


class Test_DemoBlazeEndToEndFlow:
    driver = None
    valid_username = None
    last_product = None

    '''
        following test case is parameterized based covers:-
        negative scenario --> sign up of already singed up user
        positive scenario --> new user sign up 
    '''

    @pytest.mark.parametrize("username,password",
                             [("test_user", "admin"), ("test_user" + FU.get_random_string(3), "admin")])
    @pytest.mark.usefixtures("setup", "timeStamp")
    def test_TCID_101_sign_up_to_demo_blaze(self, setup, username, password):
        test_data = ExcelUtil.get_excel_data("InputTestData.xlsx",
                                             "test_TCID_101_sign_up_to_demo_blaze")
        self.__class__.driver = setup
        home_page = HomePage(self.driver)
        home_page.click_on_navigation_menu(test_data["Navigation Option"])
        sign_up_page = SignUpPage(self.driver)
        self.__class__.valid_username = username
        sign_up_page.enter_username(self.valid_username)
        sign_up_page.enter_password(password)
        sign_up_page.click_sign_up()
        sign_up_page.verify_new_user_signup()

    '''
        following test case is parameterized based covers:-
        negative scenario --> invalid login with wrong password
        positive scenario --> valid login condition
    '''

    @pytest.mark.parametrize("password",
                             ["admin_123", "admin"])
    @pytest.mark.usefixtures("timeStamp")
    def test_TCID_102_login_to_demo_blaze(self, password):
        test_data = ExcelUtil.get_excel_data("InputTestData.xlsx",
                                             "test_TCID_102_login_to_demo_blaze")
        home_page = HomePage(self.driver)
        home_page.click_on_navigation_menu(test_data["Navigation Option"])
        login_page = LoginPage(self.driver)
        login_page.enter_username(self.valid_username)
        login_page.enter_password(password)
        login_page.click_login(self.valid_username)

    '''
        following test case verifies user can navigate products categories
    '''

    @pytest.mark.usefixtures("timeStamp")
    def test_TCID_103_Verify_product_categories_can_be_navigated_successfully(self):
        test_data = ExcelUtil.get_excel_data("InputTestData.xlsx",
                                             "test_TCID_103_Verify_product_categories_can_be_navigated_successfully")
        home_page = HomePage(self.driver)
        home_page.select_category(test_data["category_1"])
        home_page.verify_products_are_visible(test_data["mob_product_1"], test_data["mob_product_2"],
                                              test_data["mob_product_3"])
        home_page.select_category(test_data["category_2"])
        home_page.verify_products_are_visible(test_data["lap_product_1"], test_data["lap_product_2"],
                                              test_data["lap_product_3"])
        home_page.select_category(test_data["category_3"])
        home_page.verify_products_are_visible(test_data["mon_product_1"], test_data["mon_product_2"])

    '''
        following test case covers:-
         --> user can add last product
         --> user can checkout by adding product to cart
    '''

    @pytest.mark.usefixtures("timeStamp")
    def test_TCID_104_adding_products_to_shopping_cart_and_checkout(self):
        test_data = ExcelUtil.get_excel_data("InputTestData.xlsx",
                                             "test_TCID_104_adding_products_to_shopping_cart_and_checkout")
        home_page = HomePage(self.driver)
        home_page.click_on_navigation_menu(test_data["Navigation Option_1"])
        home_page.scroll_to_bottom()
        home_page.click_on_next()
        self.__class__.last_product = home_page.click_on_last_product()
        home_page.add_product_to_cart()
        home_page.click_on_navigation_menu(test_data["Navigation Option_2"])
        home_page.verify_added_product(self.last_product)
        home_page.place_order()
        home_page.enter_name("test_name_")
        home_page.enter_country("test_country_")
        home_page.enter_city("test_city_")
        home_page.enter_credit_card_details()
        home_page.enter_month("November")
        home_page.enter_year("2024")
        home_page.click_purchase()
        home_page.verify_purchase(True)
        home_page.accept_purchase()

    '''
        following test case fails as it verifies:-
         --> user can place order of the empty cart
         --> user can checkout without adding product to cart
    '''

    @pytest.mark.usefixtures("timeStamp", "teardown")
    def test_TCID_105_Attempt_to_checkout_without_adding_any_products_to_the_cart(self):
        test_data = ExcelUtil.get_excel_data("InputTestData.xlsx",
                                             "test_TCID_105_Attempt_to_checkout_without_adding_any_products_to_the_cart")
        home_page = HomePage(self.driver)
        home_page.click_on_navigation_menu(test_data["Navigation Option_1"])
        home_page.place_order()
        home_page.enter_name("test_name_")
        home_page.enter_country("test_country_")
        home_page.enter_city("test_city_")
        home_page.enter_credit_card_details()
        home_page.enter_month("November")
        home_page.enter_year("2024")
        home_page.click_purchase()
        home_page.verify_purchase(False)
        home_page.accept_purchase()

    '''
        following test case verifies user:-
         --> user can login to application 
         --> user can logout from the home page
    '''

    @pytest.mark.usefixtures("setup", "timeStamp")
    def test_TCID_106_logout_demo_blaze(self, setup):
        test_data = ExcelUtil.get_excel_data("InputTestData.xlsx",
                                             "test_TCID_106_logout_demo_blaze")
        self.__class__.driver = setup
        home_page = HomePage(self.driver)
        time.sleep(4)
        home_page.click_on_navigation_menu("Log in")
        login_page = LoginPage(self.driver)
        login_page.enter_username(self.valid_username)
        login_page.enter_password("admin")
        login_page.click_login(self.valid_username)
        home_page.click_on_navigation_menu(test_data["Navigation Option_1"])
        home_page.verify_successful_logout()
