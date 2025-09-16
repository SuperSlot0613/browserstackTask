import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#This Method is used for to send Driver Object to test method
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # or "--headless"
    options.add_argument("--no-sandbox")  # important for Docker
    options.add_argument("--disable-dev-shm-usage")  # prevents crashes
    options.add_argument("--disable-gpu")  # safe for headless
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://www.amazon.in/')
    yield driver
    driver.close()

