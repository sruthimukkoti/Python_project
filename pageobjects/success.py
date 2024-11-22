from selenium.webdriver.common.by import By


class SuccessPage:
    def __init__(self, driver):
        self.driver = driver

    country_field = (By.CSS_SELECTOR, '#country')
    country_list = (By.XPATH, '//div[@class="suggestions"]/ul/li/a')
    checkbox = (By.CSS_SELECTOR, 'label[for="checkbox2"]')
    success_btn = (By.XPATH, '//input[contains(@class,"btn-success")]')
    message_text = (By.CSS_SELECTOR, 'div[class*="alert"]')

    def entering_county_field(self):
        return self.driver.find_element(*self.country_field).send_keys('Ind')

    def countries_list(self):
        return self.driver.find_elements(*self.country_list)

    def selecting_country(self, country_name):
        countries = self.countries_list()
        try:
            for country in countries:
                name = country.text
                if name == country_name:
                    country.click()
        except Exception as e:
            print(e)

    def click_checkbox(self):
        return self.driver.find_element(*self.checkbox).click()

    def success_button(self):
        return self.driver.find_element(*self.success_btn).click()

    def success_message(self):
        return self.driver.find_element(*self.message_text)

    def get_success_message_text(self):
        message = self.success_message().text
        return message



