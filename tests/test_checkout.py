import pytest
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage

@pytest.mark.usefixtures("setup")
class TestCheckout:

    def test_add_to_cart_and_checkout(self):
        home_page = HomePage(self.driver)
        product_page = ProductPage(self.driver)
        checkout_page = CheckoutPage(self.driver)

        home_page.open_home_page()
        home_page.search_product("Laptop")
        home_page.click_first_product()
        
        # Switch to the new tab
        self.driver.switch_to.window(self.driver.window_handles[1])

        product_page.add_to_cart()
        assert product_page.is_product_added_to_cart(), "Product not added to cart"
        
        checkout_page.proceed_to_checkout()
        assert checkout_page.is_checkout_page_loaded(), "Failed to load checkout page"

        # Close the current tab and switch back to the original tab
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
