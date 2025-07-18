import pytest
from selenium import webdriver


#This Method is used for to send Driver Object to test method
@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://www.amazon.in/')
    yield driver
    driver.close()

