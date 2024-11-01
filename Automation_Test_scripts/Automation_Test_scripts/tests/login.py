import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize the Chrome WebDriver
        serv_obj = Service(r"C:\Users\SUBHAKAR\Documents\Prammu\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=serv_obj)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # Quit the driver

    def test_login_valid_credentials(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/v1/index.html")
        
        # Log in to the application
        driver.find_element(By.ID, "user-name").send_keys("standard_user") 
        driver.find_element(By.ID, "password").send_keys("secret_sauce") 
        driver.find_element(By.ID, "login-button").click()

        # Wait for the title to change and check if login was successful
        WebDriverWait(driver, 10).until(EC.title_contains("Swag Labs"))

        # Assert the page title to confirm successful login
        self.assertIn("Swag Labs", driver.title, "Login failed or timeout occurred.")

    def test_login_invalid_credentials(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/v1/index.html")
        
        # Log in to the application with invalid credentials
        driver.find_element(By.ID, "user-name").send_keys("standard") 
        driver.find_element(By.ID, "password").send_keys("sauce") 
        driver.find_element(By.ID, "login-button").click()

        # Wait for the error message to be displayed
        error_message_locator = (By.XPATH, '//*[@id="login_button_container"]/div/form/h3')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(error_message_locator))

        # Assert for error message text
        error_message = driver.find_element(*error_message_locator).text
        self.assertIn("Epic sadface: Username and password do not match any user in this service", error_message, "Error message is not displayed correctly")
        

if __name__ == '__main__':
    unittest.main()
