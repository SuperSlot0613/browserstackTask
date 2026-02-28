from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import allure


class SearchResultPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # This method is used to click on a product at a given position in the search results
    def click_on_product_by_position(self, position):
        all_search_result = self.wait.until(
            ec.presence_of_all_elements_located((By.XPATH, '//div[@role="listitem"]//h2')))

        with allure.step(f"Verify at least {position} products are listed"):
            assert len(all_search_result) >= position, (
                f"Expected: At least {position} products in results. "
                f"Actual: Found {len(all_search_result)}"
            )

        target = all_search_result[position - 1]
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", target)

        with allure.step(f"Click on product at position {position}"):
            target.click()

