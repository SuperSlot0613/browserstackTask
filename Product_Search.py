import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


try:
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://www.amazon.in/')

    actions=ActionChains(driver)
    wait=WebDriverWait(driver,15)

    mobile_dropdown=wait.until(ec.visibility_of_element_located((By.XPATH,'//input[@placeholder="Search Amazon.in"]')))
    mobile_dropdown.send_keys('Iphone 16'+Keys.DOWN+Keys.ENTER)

    time.sleep(1)

    product_list=wait.until(ec.visibility_of_element_located((By.XPATH,'(//div[@role="listitem"]//h2)[3]')))
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});",product_list)
    time.sleep(1)
    product_list.click()
    time.sleep(1)
    driver.save_screenshot('product_image.png')

    name_of_product=wait.until(ec.visibility_of_element_located((By.XPATH,'//div[@id="titleSection"]//span'))).text

    print('This is name of Product Name',name_of_product)

    rating_star=wait.until(ec.visibility_of_element_located((By.XPATH,'//div[@id="averageCustomerReviews"]//a//span')))
    rating_value=str(rating_star.text)

    print('This is rating',rating_value)

    product_mrp=wait.until(ec.visibility_of_element_located((By.XPATH,
                                                             '//div[@class="a-section a-spacing-small aok-align-center"]//span[@class="a-offscreen"]//following-sibling::span')))
    product_actual_mrp=str(product_mrp.text)
    print('This is MRP Of Product',product_actual_mrp)

    discounted_price=wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                  '//div[@class="a-section a-spacing-none aok-align-center aok-relative"]//span[@class="a-price-whole"]')))
    print('This is Discounted Price ₹',str(discounted_price.text))

    discounte_percentage=wait.until(ec.visibility_of_element_located((By.XPATH,
                                                                      '//div[@class="a-section a-spacing-none aok-align-center aok-relative"]//span//following-sibling::span')))
    print('This is discounted percentage',str(discounte_percentage.text).replace('-',''))


except Exception as e:
    print('Error come dur to this',e)



