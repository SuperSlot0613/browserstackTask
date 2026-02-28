# BrowserStack Task — Amazon Product Search Automation

Selenium-based test automation for Amazon.in product search, built with the **Page Object Model** pattern, **pytest**, and **Allure** reporting.

## Project Structure

```
├── Pages/                  # Page Object classes
│   ├── HomePage.py         # Home page interactions (search, page validation)
│   ├── SearchResultPage.py # Search results interactions (product selection)
│   └── ProductViewDetail.py# Product detail page (name, price, rating)
├── Test/
│   └── test_product_search.py  # Test cases
├── conftest.py             # pytest fixtures (WebDriver setup)
├── Product_Search.py       # Standalone search script
├── Dockerfile              # Docker image for running tests
├── Jenkinsfile             # CI/CD pipeline definition
└── requirements.txt        # Python dependencies
```

## Prerequisites

- Python 3.11+
- Google Chrome & ChromeDriver

## Setup

```bash
pip install -r requirements.txt
```

## Running Tests

```bash
# Run all tests
pytest -v -s --alluredir=allure-results

# Run a specific test
pytest Test/test_product_search.py::test_product_validation_of_third_product -v -s
```

## Running with Docker

```bash
docker build -t browserstacktask .
docker run --shm-size=2g browserstacktask
```

## Allure Reports

After running tests with `--alluredir=allure-results`:

```bash
allure serve allure-results
```
