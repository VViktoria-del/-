import allure
from tests.pages.popups_page import PopupsPage

@allure.epic("Practice Automation")
@allure.feature("Popups Page")
def test_open_and_close_popup(driver):
    page = PopupsPage(driver)
    page.open()
    with allure.step("Открываем popup"):
        page.open_popup()
    assert page.is_popup_visible()
    with allure.step("Закрываем popup"):
        page.close_popup()
    assert not page.is_popup_visible()
