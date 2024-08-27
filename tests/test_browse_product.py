import pytest
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup")
class TestBrowsing:

    def test_browsing_product_category(self):
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        home_page.select_category("Electronics")  # Example category
        assert home_page.is_category_selected("Electronics"), "Failed to browse to category: Electronics"

    def test_search_functionality(self):
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        home_page.search_product("Laptop")
        assert home_page.is_product_listed("Laptop"), "Search functionality failed for product: Laptop"
