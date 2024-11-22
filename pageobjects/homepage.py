from selenium.webdriver.common.by import By
from pageobjects.checkout import checkout_page


class homepage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, 'a[href*="/shop"]')

    def shop_items(self):
        return self.driver.find_element(*self.shop) #we can call variables with self method

    def click_shop_items(self):
        self.shop_items().click()
        checkout = checkout_page(self.driver)
        return checkout

