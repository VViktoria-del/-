from selenium.webdriver.common.by import By
from .base_page import BasePage

class PopupsPage(BasePage):
    URL = "https://practice-automation.com/popups/"
    OPEN_BTN = (By.XPATH, "//button[contains(.,'Show Popup')]")
    POPUP = (By.CSS_SELECTOR, ".pum-active")
    CLOSE_BTN = (By.CSS_SELECTOR, ".pum-active button")

    def open(self):
        super().open(self.URL)

    def open_popup(self):
        self.find(*self.OPEN_BTN).click()

    def close_popup(self):
        self.find(*self.CLOSE_BTN).click()

    def is_popup_visible(self):
        return len(self.driver.find_elements(*self.POPUP)) > 0
