import time

from Utilities.base_class import Base
from pageobjects.homepage import homepage


class Test_Ekart(Base):

    def test_e2e(self):
        self.implicit_wait()
        home_page = self.navigation_url()
        checkout_page = home_page.click_shop_items()
        checkout_page.click_on_required_mobile("Blackberry")
        confirm_page = checkout_page.click_on_checkout_button()
        success_page = confirm_page.click_success_button()
        success_page.entering_county_field()
        self.explicit_wait()
        success_page.selecting_country('Indonesia')
        success_page.click_checkbox()
        success_page.success_button()
        message = success_page.get_success_message_text()
        assert 'Thank you!' in message
        time.sleep(5)





