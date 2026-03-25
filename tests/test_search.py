import pytest
from pages.product_page import ProductPage

@pytest.mark.smoke
def test_search_product(page, config):
    product_page = ProductPage(page)
    page.goto(config["base_url"])   # pulled from dev.yaml
    product_page.search_product("Cucumber")
    products = product_page.get_displayed_products()
    assert any("Cucumber" in p for p in products), "Search result did not display Cucumber"