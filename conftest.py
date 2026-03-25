import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def config():
    # Provide safe defaults
    return {
        "browser": "chromium",
        "headless": True
    }

@pytest.fixture(scope="function")
def page(config):
    with sync_playwright() as p:
        browser = getattr(p, config["browser"]).launch(headless=config["headless"])
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()