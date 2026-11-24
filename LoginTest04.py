
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.saucedemo.com"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()


def login(username, password):
    driver.get(URL)
    time.sleep(2)
    driver.find_element(By.ID, "user-name").send_keys(username)
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(2)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)


def check(test_name, condition):
    if condition:
        print(test_name, "- Passed")
    else:
        print(test_name, "- Failed")


# Test 1: valid login
login("standard_user", "secret_sauce")
check("Test 1: valid login", "inventory" in driver.current_url)

# Test 2: add product to cart
time.sleep(2)
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(2)
badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
check("Test 2: add product to cart", badge == "1")

# Test 3: logout
time.sleep(2)
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(2)
driver.find_element(By.ID, "logout_sidebar_link").click()
time.sleep(3)
check("Test 03 logout", driver.find_element(By.ID, "login-button").is_displayed)

# Test 4: locked out user
driver = webdriver.Chrome(options=options)
driver.maximize_window()
login("locked_out_user", "secret_sauce")
time.sleep(2)
error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
check("Test 4: locked out user", "locked out user" in error.lower())
print("\nAll tests completed!")
