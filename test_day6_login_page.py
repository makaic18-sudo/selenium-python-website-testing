from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def logn(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.fin_element(By.ID, "login-button").click()

    def get_error(self):
        wait = WebDriverWait(self.driver, 10)
        error = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "[data-test='error']")))
        return error.text