from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com")
driver.find_element(By.ID, "user-name").send_keys("visual_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
if "inventory" in driver.current_url:
    print("Test Passed: User can Log In")
else:
    print("Test Failed: User can't Log In")
driver.quit()