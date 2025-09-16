from Pages.HomePage import HomePage
from Pages.SearchResultPage import SearchResultPage
from Pages.ProductViewDetail import ProductViewDetail
import allure


# This test method test the Search,resukt check and Product detail fetch Functionality
@allure.feature("Product")
@allure.story("Successfully Validated Product")
def test_product_validation_of_third_product(driver):
    home_page=HomePage(driver)
    search_result=SearchResultPage(driver)
    product_detail=ProductViewDetail(driver)

    home_page.validated_home_page_open()
    home_page.search_product('Iphone 16')
    search_result.click_on_third_result(3)
    # product_detail.get_product_detail()


# def test_product_validation_of_fifth_product(driver):
#     home_page=HomePage(driver)
#     search_result=SearchResultPage(driver)
#     product_detail=ProductViewDetail(driver)
#
#     home_page.validated_home_page_open()
#     home_page.search_product('Oneplus')
#     search_result.click_on_third_result(5)
#     product_detail.get_product_detail()

