import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    """Set up and tear down the Chrome WebDriver for each test."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://www.amazon.in/')
    yield driver
    driver.quit()
