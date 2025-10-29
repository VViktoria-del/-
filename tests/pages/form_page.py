from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage

class FormPage(BasePage):
    URL = "https://practice-automation.com/form-fields/"
    MESSAGE = (By.ID, "message")
    TOOLS_SELECT = (By.XPATH, "//label[contains(., 'Automation Tools')]/following::select[1]")

    def open(self):
        super().open(self.URL)

    def get_automation_tools(self):
        select_elem = self.find(*self.TOOLS_SELECT)
        select = Select(select_elem)
        return [opt.text for opt in select.options if opt.text.strip()]

    def fill_message_with_tools(self):
        tools = self.get_automation_tools()
        message = ", ".join(tools)
        message_field = self.find(*self.MESSAGE)
        message_field.clear()
        message_field.send_keys(message)
        return message
