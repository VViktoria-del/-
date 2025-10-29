import allure
from tests.pages.click_events_page import ClickEventsPage

@allure.epic("Practice Automation")
@allure.feature("Click Events")
def test_click_events(driver):
    page = ClickEventsPage(driver)
    page.open()
    with allure.step("Выполняем клики (single, double, right)"):
        page.perform_clicks()
