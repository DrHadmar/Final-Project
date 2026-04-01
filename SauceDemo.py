from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

import time

# Path to GeckoDriver & Firefox
service = Service("C:/Users/Dr. Hadmar/Documents/Dropbox/Software Testing/Code/geckodriver-v0.36.0-win32/geckodriver.exe")
options = Options()
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"

# Start browser
driver = webdriver.Firefox(service=service, options=options)

# Go to Website
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Check
if "inventory" in driver.current_url:
    print("Login successful")
else:
    print("Login failed")

# get some time to actually see the site
time.sleep(10)

driver.quit()





