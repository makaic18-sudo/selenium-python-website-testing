#DAY 02
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
URL = "https://www.saucedemo.com/"
driver=webdriver.Chrome()
driver.get(URL)
driver.maximize_window()
time.sleep(5)
#Test 02: Logging In with wrong Credentials
driver.get(URL)
time.sleep(5)
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(5)
driver.find_element(By.ID, "password").send_keys("King Ali")
time.sleep(5)
driver.find_element(By.ID, "login-button").click()
time.sleep(5)
error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
print("Error Shown", error)
if "Do not match" in error:
    print("Test 01 Passed: Wrong credentials so user cannot Log In")
else:
    print("Test 01 Failed")
input("Please press Enter to close the browser...")
driver.quit()