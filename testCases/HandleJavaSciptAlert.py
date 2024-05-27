import time
import pytest
from pageFactory.javaScriptPage import JavaScriptPage
from generic.ExcelUtil import ExcelUtil


class Test_HandelJavaScript:
    driver = None

    @pytest.mark.usefixtures("setup", "timeStamp")
    def test_handle_javascript(self, setup):
        test_data = ExcelUtil.get_excel_data("InputTestData.xlsx", "test_handle_javascript")
        key = test_data["set_text"]
        self.__class__.driver = setup
        java_script_page = JavaScriptPage(self.driver)
        java_script_page.click_on_alert()
        time.sleep(3)
        java_script_page.click_js_confirm()
        time.sleep(3)
        java_script_page.click_and_set_text_on_JS_prompt(key)
        time.sleep(3)
