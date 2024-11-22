from selenium.webdriver.common.by import By
from pageobjects.success import SuccessPage


class confirmpage:
    def __init__(self, driver):
        self.driver = driver

    success_btn = (By.CSS_SELECTOR, 'button[class*="btn-success"]')

    def success_button(self):
        return self.driver.find_element(*self.success_btn)

    def click_success_button(self):
        self.success_button().click()
        successpage = SuccessPage(self.driver)
        return successpage


