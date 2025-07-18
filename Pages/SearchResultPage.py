from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class SearchResultPage:

    def __init__(self,driver : WebDriver):
        self.driver=driver
        self.wait=WebDriverWait(driver,15)
        self.actions=ActionChains(driver)

    # This method is used for to select specific number of product from search result
    def click_on_third_result(self,num_product_click):

        all_search_result=self.wait.until(ec.presence_of_all_elements_located((By.XPATH,'//div[@role="listitem"]//h2')))

        count=0

        for index,element in enumerate(all_search_result):
            if index==(num_product_click-1):
                self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
                element.click()
                break
            count+=1

        print('This is count',count)

        assert count==(num_product_click-1),f"Expected : User should able to Click Third Product But Actual : User is not able to click on Third Product"


