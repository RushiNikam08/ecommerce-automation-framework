# pages/product_page.py
from locators import product_locators

class ProductPage:
    def __init__(self, page):
        self.page = page

    def search_product(self, name: str):
        self.page.fill(product_locators.SEARCH_BOX, name)

    def get_displayed_products(self):
        return self.page.locator(product_locators.PRODUCT_NAME).all_text_contents()