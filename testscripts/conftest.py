import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utilities.logger import setup_logger
import yaml
import os

# ----------------- Load config -----------------
config_path = os.path.join(os.path.dirname(__file__), "config", "config.yaml")
with open(config_path, 'r') as file:
    config = yaml.safe_load(file)

logger = setup_logger("OrangeHRM_Automation")

# ----------------- PyTest Fixtures -----------------
@pytest.fixture(scope="session")
def driver():
    """Initialize WebDriver for the session"""
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    service = Service()  # Ensure chromedriver is in PATH or specify executable_path
    driver = webdriver.Chrome(service=service, options=options)
    logger.info("WebDriver session started")
    yield driver
    driver.quit()
    logger.info("WebDriver session closed")

@pytest.fixture(scope="session")
def base_url():
    return config['url']

@pytest.fixture(scope="session")
def credentials():
    return config['credentials']

# ----------------- Screenshot on failure -----------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver_fixture = item.funcargs.get('driver')
        if driver_fixture:
            screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            file_name = os.path.join(screenshot_dir, f"{item.name}.png")
            driver_fixture.save_screenshot(file_name)
            logger.error(f"Test failed. Screenshot saved at {file_name}")
