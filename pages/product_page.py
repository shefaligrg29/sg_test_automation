from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException

class ProductPage(BasePage):

    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def add_to_cart(self):
        add_to_cart_button = (By.ID, "add-to-cart-button")
        add_to_cart_element = self.scroll_to_element(add_to_cart_button)
        
        for _ in range(3):  # Retry up to 3 times
            try:
                add_to_cart_element.click()
                break  # Break if click is successful
            except ElementClickInterceptedException:
                self.driver.execute_script("window.scrollBy(0, -100);")  # Adjust scroll if needed

                
    def is_product_added_to_cart(self):
        cart_success_message = (By.XPATH, "//h1[contains(text(), 'Added to Cart')]")
        return self.is_element_present(cart_success_message)
