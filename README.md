# Technical Assessment

## Project Overview

This project includes automated test scripts for core functionality on (https://www.saucedemo.com/v1/index.html) website. Using **Python**, **Selenium**, and the **unittest** framework, the scripts cover high-priority areas such as login,product and cart management, checkout, and product sorting. This README provides guidance on setting up, running tests, and navigating the repository.

## Folder Structure
📁 Automation Test Scripts ├── 📄 requirements.txt ├── 📄 README.md (for automation code) ├── 📄 Test_Rationale.md ├── 📂 tests │ ├── login.py │ ├── add_to_cart.py │ ├── remove_from_cart.py │ ├── checkout.py │ └── sort_products.py 

📁 Docs ├── 📄 Test_Plan.md ├── 📄 Test_Cases.md ├── 📄 Bugs.md ├── 📄 Exploratory_Testing_Documentation.md 


## Test Scope

The automated tests included in this project focus on the following functionalities to optimize testing resources, enhance efficiency, and ensure repeatability:

1. **Login Flow** - Tests for both successful and failed login scenarios to validate user authentication.
2. **Product and Cart Management** - Tests for adding and removing products from the cart, crucial for verifying the smooth management of cart operations.
3. **Checkout Process** - Full checkout workflow test, including input validation to confirm end-to-end purchase functionality.
4. **Sorting Products** - Tests for sorting products based on criteria like price and priority, ensuring users can sort items effectively.

## Technologies and Tools

- **Python**: Programming language used to create automation scripts.
- **Selenium**: Tool used for automating browser actions.
- **unittest**: Python’s built-in testing framework used for structuring and executing test cases.

## Setup Instructions

1. **Clone Repository**: 
   ```bash
   git clone https://github.com/Pramallika/Technical_Assessment_TestEng.git
2. **Navigate to Project Directory**:
   cd Technical_Assessment_TestEng
3. **Install Dependencies**:
   pip install -r "Automation Test Scripts/requirements.txt"
4. **Setup WebDriver**:
   Ensure that the appropriate WebDriver (e.g., ChromeDriver) is available and accessible in your system’s PATH.

## Running Tests

1. **Navigate to Automation Test Scripts Folder**:
   cd "Automation Test Scripts"
2. **Run All Tests**:
   python -m unittest discover -s tests -p "*.py"
3.**Run Individual Tests**:
   python -m unittest tests/login.py

## Test Rationale
The Test_Rationale.md file provides insights into the specific test cases chosen and their significance for robust, accurate regression testing.

## Documentation

Documentation files are available in the Docs folder:

Test_Plan.md: Describes the test strategy and test coverage.
Test_Cases.md: Lists each test case with details about the expected and actual results.
Bugs.md: Documents known bugs, their statuses, and additional information.
Exploratory_Testing_Documentation.md: Notes on exploratory testing activities, observations, and outcomes.

## Additional Notes

This project structure is designed to provide a clear and organized approach to automation testing for key e-commerce functionalities. Feedback and suggestions for improvements are welcome.

