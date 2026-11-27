#DAY 03
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
URL = "https://www.saucedemo.com/"
driver = webdriver.Chrome()
#Test 03: Logging In with empty fields
driver.get(URL)
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"login-button").click()
time.sleep(3)
error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
print("Error Shown", error)
if "Empty Fields error is showing" in error:
    print("Test 03: User cannot Log In with empty fields")
else:
    print("Test 03 Failed")
driver.quit()