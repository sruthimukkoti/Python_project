from selenium.webdriver.common.by import By

from pageobjects.confirm import confirmpage


class checkout_page:

    def __init__(self, driver):
        self.driver = driver

    Mobiles = (By.XPATH, '//div[@class="card h-100"]')
    checkout_btn = (By.XPATH, '//a[contains(@class,"btn-primary")]')

    def list_of_mobiles(self):
        return self.driver.find_elements(*checkout_page.Mobiles) #we can call variables with classname or self

    def click_on_required_mobile(self, mobile_name):
        mobiles_List = self.list_of_mobiles()
        for i in mobiles_List:
            name = i.find_element(By.XPATH,'div/h4/a').text
            if name == mobile_name:
                i.find_element(By.XPATH,'div/button').click()

    def checkout_button(self):
        return self.driver.find_element(*checkout_page.checkout_btn)

    def click_on_checkout_button(self):
        self.checkout_button().click()
        confirm_page = confirmpage(self.driver)
        return confirm_page


