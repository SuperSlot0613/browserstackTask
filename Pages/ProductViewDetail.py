import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class ProductViewDetail:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # This method is used to fetch and validate product details:
    # Name, Rating, MRP Price, Discounted Price, and Discount Percentage
    def get_product_detail(self):
        errors = []

        name_of_product = self.wait.until(
            ec.visibility_of_element_located((By.XPATH, '//div[@id="titleSection"]//span')))
        product_name = str(name_of_product.text)

        with allure.step(f"Verify product name is displayed: '{product_name}'"):
            try:
                assert product_name != '', "Product name should not be empty"
            except AssertionError as e:
                errors.append(str(e))

        rating_star = self.wait.until(
            ec.visibility_of_element_located((By.XPATH, '//div[@id="averageCustomerReviews"]//a//span')))
        rating_value = str(rating_star.text)

        with allure.step(f"Verify product rating is displayed: '{rating_value}'"):
            try:
                assert rating_value != '', "Product rating should not be empty"
            except AssertionError as e:
                errors.append(str(e))

        product_mrp = self.wait.until(ec.visibility_of_element_located((By.XPATH,
            '//div[@class="a-section a-spacing-small aok-align-center"]//span[@class="a-offscreen"]//following-sibling::span')))
        product_actual_mrp = str(product_mrp.text)

        with allure.step(f"Verify product MRP is displayed: '{product_actual_mrp}'"):
            try:
                assert product_actual_mrp != '', "Product MRP should not be empty"
            except AssertionError as e:
                errors.append(str(e))

        discounted_price = self.wait.until(ec.visibility_of_element_located((By.XPATH,
            '//div[@class="a-section a-spacing-none aok-align-center aok-relative"]//span[@class="a-price-whole"]')))
        discounted_price_text = str(discounted_price.text)

        with allure.step(f"Verify discounted price is displayed: '₹{discounted_price_text}'"):
            try:
                assert discounted_price_text != '', "Discounted price should not be empty"
            except AssertionError as e:
                errors.append(str(e))

        discount_percentage = self.wait.until(ec.visibility_of_element_located((By.XPATH,
            '//div[@class="a-section a-spacing-none aok-align-center aok-relative"]//span//following-sibling::span')))
        discount_text = str(discount_percentage.text).replace('-', '')

        with allure.step(f"Verify discount percentage is displayed: '{discount_text}'"):
            try:
                assert discount_text != '', "Discount percentage should not be empty"
            except AssertionError as e:
                errors.append(str(e))

        if errors:
            raise AssertionError('\n'.join(errors))