from time import sleep
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageobjects.homepage import homepage
from tests.conftest import setup
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class Base():

    def navigation_url(self):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        h_object = homepage(self.driver)
        return h_object

    def implicit_wait(self):
        return self.driver.implicitly_wait(10)

    def explicit_wait(self):
        wait = WebDriverWait(self.driver, 30)
        Locator = '//div[@class="suggestions"]/ul/li/a'
        # wait.until(expected_conditions.visibility_of_all_elements_located(By.XPATH, Locator))
        wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, Locator)))
