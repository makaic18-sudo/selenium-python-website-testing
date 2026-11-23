#Test 01: Login with Valid Username and Password
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = options)
driver.get("https://www.saucedemo.com/")
time.sleep(3)
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(3)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(3)
driver.find_element(By.ID, "login-button").click()
time.sleep(3)
if "inventory" in driver.current_url:
    print("Test Passed: User can Log In")
else:
    print("Test Failed: User cannot Log In")
driver.quit()
