from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    def open_home_page(self):
        self.driver.get("https://www.amazon.in")

    def select_category(self, category_name):
        category_locator = (By.LINK_TEXT, category_name)
        self.click(category_locator)

    def is_category_selected(self, category_name):
        category_header_locator = (By.XPATH, f"//span[contains(text(), '{category_name}')]")
        return self.is_element_present(category_header_locator)

    def search_product(self, product_name):
        search_box_locator = (By.ID, "twotabsearchtextbox")
        search_button_locator = (By.ID, "nav-search-submit-button")
        self.enter_text(search_box_locator, product_name)
        self.click(search_button_locator)

    def is_product_listed(self, product_name):
        product_locator = (By.XPATH, f"//span[contains(text(), '{product_name}')]")
        return self.is_element_present(product_locator)
    
    def click_first_product(self):
        first_product_locator = (By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result'] h2 a")
        self.click(first_product_locator)
