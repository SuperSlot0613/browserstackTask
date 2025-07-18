import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:

    def __init__(self,driver : WebDriver):
        self.driver=driver
        self.wait=WebDriverWait(driver,15)
        self.actions=ActionChains(driver)


    #This method used for to search the product
    def search_product(self,product_name):

        mobile_dropdown = self.wait.until(
            ec.visibility_of_element_located((By.XPATH, '//input[@placeholder="Search Amazon.in"]')))
        mobile_dropdown.send_keys(product_name)
        time.sleep(2)
        mobile_dropdown.send_keys(Keys.DOWN+Keys.ENTER)

        result_name=self.wait.until(ec.visibility_of_element_located((By.XPATH,'(//div[@role="listitem"]//h2//span)[1]')))

        assert 'iphone' in str(result_name.text).lower(),\
            f"Expected : The result should come for this Product {product_name} Actual : The result is coming for Some other Product {str(result_name.text)}"

    #This method is used for to check the Chrome is open or not
    def validated_home_page_open(self):
        home_page_text=self.wait.until(ec.presence_of_element_located((By.XPATH,'//div[@class="nav-line-1-container"]//span')))
        assert 'Hello, sign in'==home_page_text.text,f"Expected : Home Page Should Open Actual : Home Page Taking to Much Time to Open"