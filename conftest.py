import pytest
from playwright.sync_api import sync_playwright
from utils.config_reader import load_config

def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="dev", help="Environment to run tests against"
    )

@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    return load_config(env=env)

@pytest.fixture(scope="function")
def page(config):
    with sync_playwright() as p:
        browser = getattr(p, config["browser"]).launch(headless=config["headless"])
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

