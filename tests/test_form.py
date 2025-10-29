import allure
from tests.pages.form_page import FormPage

@allure.epic("Practice Automation")
@allure.feature("Form Page")
def test_fill_message_with_tools(driver):
    page = FormPage(driver)
    page.open()
    with allure.step("Заполняем поле Message списком Automation Tools"):
        message = page.fill_message_with_tools()
    value = driver.find_element("id", "message").get_attribute("value")
    assert message == value
