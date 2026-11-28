import pytest
from selenium import webdriver
from login_page import LoginPage

def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_with_valid_login(driver):
    page = LoginPage
    page.open()
    page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

def test_with_wrong_password(driver):
    page = LoginPage
    page.open()
    page.login("standard_user", "wrong_password")
    assert "do not match" in page.get_error()

def test_with_locked_out_user(driver):
    page = LoginPage
    page.open()
    page.login("locked_out_user", "secret_sauce")
    assert "locked_out_user" in page.get_error()