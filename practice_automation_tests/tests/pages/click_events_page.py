from selenium.webdriver.common.by import By
from .base_page import BasePage

class ClickEventsPage(BasePage):
    URL = "https://practice-automation.com/click-events/"
    DOUBLE = (By.ID, "double-click")
    RIGHT = (By.ID, "right-click")
    SINGLE = (By.ID, "click")

    def open(self):
        super().open(self.URL)

    def perform_clicks(self):
        from selenium.webdriver import ActionChains
        actions = ActionChains(self.driver)
        actions.click(self.find(*self.SINGLE)).perform()
        actions.double_click(self.find(*self.DOUBLE)).perform()
        actions.context_click(self.find(*self.RIGHT)).perform()
