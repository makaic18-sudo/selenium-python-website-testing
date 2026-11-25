import time 
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    time.sleep(3)
    driver.quit()

def login(driver, username, password):
    time.sleep(3)
    driver.find_element(By.ID, "user-name").send_keys(username)
    time.sleep(3)
    driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(3)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

def test_valid_login(driver):
    login(driver, "standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

def test_wrong_password(driver):
    login(driver, "standard_user", "wrong_password")
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "do not match" in error

def test_empty_fields(driver):
    login(driver, "", "")
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "Username is required" in error