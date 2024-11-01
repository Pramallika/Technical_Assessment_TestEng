import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

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

    def test_sort_by_price_low_to_high(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get("https://www.saucedemo.com/v1/index.html")
        
        # Log in to the application
        driver.find_element(By.ID, "user-name").send_keys("standard_user") 
        driver.find_element(By.ID, "password").send_keys("secret_sauce") 
        driver.find_element(By.ID, "login-button").click()
        time.sleep(5)

        #sort products by price(low to high)
        sort_dropdown = Select(driver.find_element(By.XPATH, '//*[@id="inventory_filter_container"]/select'))
        sort_dropdown.select_by_visible_text("Price (low to high)")
        time.sleep(5)

        #verify sort - pseudo-check for sorted prices
        price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        prices = []

        for price_element in price_elements:
            # Extract text and remove the dollar sign and convert to float
            price_text = price_element.text.replace('$', '')
            prices.append(float(price_text))  # Convert to float

        # Check if prices are sorted in ascending order
        self.assertEqual(prices, sorted(prices), "The prices are not sorted from low to high!")
        
       

if __name__ == '__main__':
    unittest.main()