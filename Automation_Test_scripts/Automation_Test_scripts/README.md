# SauceDemo Automation Test Suite

This project automates functional testing for the [SauceDemo](https://www.saucedemo.com/v1/index.html) website using Python and Selenium with the `unittest` framework.

## Project Structure

saucedemo_tests/
│
├── tests/
│ ├── test_login.py # Test login functionality
│ ├── test_add_to_cart.py # Test adding items to cart
│ ├── test_remove_from_cart.py # Test removing items from cart
│ ├── test_sort_products.py # Test product sorting functionality
│ ├── test_checkout.py # Test checkout flow
│
├── requirements.txt # Dependencies
└── README.md # Project overview and setup instructions

## Setup Instructions

### Prerequisites

1. **Python**: Ensure Python 3.7 or later is installed. [Download Python](https://www.python.org/downloads/).
2. **Chrome**: Make sure you have the latest version of Google Chrome installed.
3. **ChromeDriver**: This will be managed automatically by `webdriver-manager`.

### Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd saucedemo_tests

2. Install the required Python packages:

pip install -r requirements.txt



Running the Tests

Each test file is self-contained and can be run individually, or you can run all tests together using unittest.

Run All Tests

To run all tests in the tests directory, use the following command:

python -m unittest discover -s tests

Run Individual Tests

To run an individual test file, specify the file directly:

python -m unittest tests/test_login.py

Test Descriptions

• test_login.py: Verifies that a valid user can successfully log in to the site.
• test_add_to_cart.py: Adds a specific item to the cart and verifies it appears in the cart.
• test_remove_from_cart.py: Adds an item, removes it from the cart, and confirms it’s no longer present.
• test_sort_products.py: Tests the product sorting functionality, specifically sorting by price (low to high).
• test_checkout.py: Completes the checkout flow by filling in customer information and confirming it proceeds as expected.

Troubleshooting

1. ChromeDriver Issues: If ChromeDriver is not compatible with your version of Chrome, update it automatically using webdriver-manager.
• To manually clear ChromeDriver cache, run:

webdriver-manager clean


2. Timeouts: If elements are not loading quickly enough, increase the implicitly_wait time in each test’s setUpClass method.
3. Selenium and ChromeDriver Logs: If tests fail unexpectedly, check the console for Selenium and ChromeDriver logs, which can provide insights into issues with element location or page load.

This README.md provides everything you need to set up, run, and troubleshoot the tests.