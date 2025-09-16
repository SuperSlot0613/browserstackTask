import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class ProductViewDetail:

    def __init__(self,driver : WebDriver):
        self.driver=driver
        self.wait=WebDriverWait(driver,15)
        self.actions=ActionChains(driver)


    # This method is used for to fetch product Name,rating,MRP Price,Discounted Price and Discount Percentage
    def get_product_detail(self):
        time.sleep(2)
        error=[]

        name_of_product = self.wait.until(
            ec.visibility_of_element_located((By.XPATH, '//div[@id="titleSection"]//span')))

        print('This is name of Product Name', str(name_of_product.text))

        try:
            assert str(name_of_product.text)!='',f'Expected : User Should able to get product Name Actual : User are getting {str(name_of_product.text)}'
        except AssertionError as e:
            error.append(f'Expected : User Should able to get product Name Actual : User are getting {str(name_of_product.text)}')


        rating_star = self.wait.until(
            ec.visibility_of_element_located((By.XPATH, '//div[@id="averageCustomerReviews"]//a//span')))
        rating_value = str(rating_star.text)

        print('This is rating', rating_value)

        try:
            assert rating_value!='',f'Expected : User Should able to see Rating Actual : User is not able to see {rating_value}'
        except AssertionError as e:
            error.append(f'Expected : User Should able to see Rating Actual : User is not able to see {rating_value}')

        product_mrp = self.wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                   '//div[@class="a-section a-spacing-small aok-align-center"]//span[@class="a-offscreen"]//following-sibling::span')))
        product_actual_mrp = str(product_mrp.text)
        print('This is MRP Of Product', product_actual_mrp)

        try:
            assert product_actual_mrp!='',f'Expected : User Should able to see Product MRP Actual : User is getting {product_actual_mrp}'
        except AssertionError as e:
            error.append(f'Expected : User Should able to see Product MRP : User is getting {product_actual_mrp}')

        discounted_price = self.wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                        '//div[@class="a-section a-spacing-none aok-align-center aok-relative"]//span[@class="a-price-whole"]')))
        print('This is Discounted Price ₹', str(discounted_price.text))

        try:
            assert str(discounted_price.text)!='',f'Expected : User Should able to see Discounted Price Actual : User is getting {str(discounted_price.text)}'
        except AssertionError as e:
            error.append(f'Expected : User Should able to see Discounted Price Actual : User is getting {str(discounted_price.text)}')

        discounte_percentage = self.wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                            '//div[@class="a-section a-spacing-none aok-align-center aok-relative"]//span//following-sibling::span')))
        print('This is discounted percentage', str(discounte_percentage.text).replace('-', ''))

        try:
            disc_text = str(discounte_percentage.text).replace('-', '')
            assert disc_text != '', (
                f"Expected: User should be able to see Discounted percentage. "
                f"Actual: User is getting {disc_text}"
            )
        except AssertionError as e:
            error.append(f'Expected : User Should able to see Discounted percentage Actual : User is getting {str(discounte_percentage.text).replace('-', '')}')


        if error:
            raise AssertionError('\n'.join(error))


#vinod@browserstack.com