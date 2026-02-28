from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import allure


class HomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # This method is used to search for a product
    def search_product(self, product_name):
        search_box = self.wait.until(
            ec.visibility_of_element_located((By.XPATH, '//input[@placeholder="Search Amazon.in"]')))
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.ENTER)

        result_name = self.wait.until(
            ec.visibility_of_element_located((By.XPATH, '(//div[@role="listitem"]//h2//span)[1]')))

        result_text = str(result_name.text).lower()
        search_term = product_name.lower().split()[0]

        with allure.step(f"Verify search results contain '{product_name}'"):
            assert search_term in result_text, (
                f"Expected: Results for '{product_name}'. "
                f"Actual: Got '{result_name.text}'"
            )

    # This method is used to verify the home page is loaded
    def validated_home_page_open(self):
        home_page_text = self.wait.until(
            ec.presence_of_element_located((By.XPATH, '//div[@class="nav-line-1-container"]//span')))
        with allure.step("Verify Amazon home page is loaded"):
            assert home_page_text.text is not None, (
                f"Expected: Home page text to be present. "
                f"Actual: Got '{home_page_text.text}'"
            )