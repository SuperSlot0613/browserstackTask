from Pages.HomePage import HomePage
from Pages.SearchResultPage import SearchResultPage
from Pages.ProductViewDetail import ProductViewDetail
import allure


@allure.feature("Product Search")
@allure.story("Search and validate third product in results")
def test_product_validation_of_third_product(driver):
    home_page = HomePage(driver)
    search_result = SearchResultPage(driver)

    home_page.validated_home_page_open()
    home_page.search_product('Iphone 16')
    search_result.click_on_product_by_position(3)


@allure.feature("Product Search")
@allure.story("Search and validate fifth product in results")
def test_product_validation_of_fifth_product(driver):
    home_page = HomePage(driver)
    search_result = SearchResultPage(driver)

    home_page.validated_home_page_open()
    home_page.search_product('Oneplus')
    search_result.click_on_product_by_position(5)

