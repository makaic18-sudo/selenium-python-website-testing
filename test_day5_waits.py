import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    time.sleep(3)
    driver.quit()

def test_login_wait(driver):
    time.sleep(2)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.ID, "login-button").click()

    wait = WebDriverWait(driver, 10)
    time.sleep(2)
    title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
    assert title.text == "Products"

def test_add_to_cart_with_wait(driver):
    time.sleep(2)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.ID, "login-button").click()

    wait = WebDriverWait(driver, 10)
    time.sleep(2)
    button = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    button.click()

    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"