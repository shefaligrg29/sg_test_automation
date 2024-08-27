from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):

    def proceed_to_checkout(self):
        checkout_button = (By.ID, "hlb-ptc-btn-native")
        self.click(checkout_button)

    def is_checkout_page_loaded(self):
        checkout_page_header = (By.XPATH, "//h1[contains(text(), 'Checkout')]")
        return self.is_element_present(checkout_page_header)
