
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    def test_add_to_cart(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get("https://www.saucedemo.com/v1/index.html")
        
        # Log in to the application
        driver.find_element(By.ID, "user-name").send_keys("standard_user") 
        driver.find_element(By.ID, "password").send_keys("secret_sauce") 
        driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
       

        # Add item to cart
        driver.find_element(By.XPATH, "//div[@class='inventory_item'][2]//button[text()='ADD TO CART']").click()
        time.sleep(5)
        #verify item in cart
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(5)
        self.assertIn("Sauce Labs Bike Light", driver.page_source, "Item not added")

        #proceed to checkout
        driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[2]/a[2]').click()
       
        #fill checkout information
        first_name_input = self.driver.find_element(By.ID, 'first-name')
        first_name_input.send_keys("Joe")

        last_name_input = self.driver.find_element(By.ID, 'last-name')
        last_name_input.send_keys("William")
        
        zip_code_input = self.driver.find_element(By.ID, 'postal-code')
        zip_code_input.send_keys('TA$%DF')

        driver.find_element(By.XPATH,'//*[@id="checkout_info_container"]/div/form/div[2]/input').click()
        time.sleep(5)
        driver.find_element(By.XPATH,'//*[@id="checkout_summary_container"]/div/div[2]/div[8]/a[2]').click()

        #Order confirmation
        self.assertIn("THANK YOU FOR YOUR ORDER", driver.page_source, "Order not placed")
        

        

if __name__ == '__main__':
    unittest.main()
