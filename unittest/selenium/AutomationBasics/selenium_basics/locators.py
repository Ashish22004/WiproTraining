import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

# Use this - Selenium will automatically find/download the correct driver
driver = webdriver.Edge()

driver.get("https://www.google.com")

# ID locator
'''search_input = driver.find_element(By.ID, value="APjFqb")
search_input.send_keys("selenium")
search_input.clear()'''

# NAME
search_input = driver.find_element(By.NAME, "q")
search_input.send_keys("locators")

# ERROR FIX: Use JavaScript to click the button because it is physically
# overlapped by the search suggestions dropdown.
googlesearch_button = driver.find_element(By.NAME, "btnK")
driver.execute_script("arguments[0].click();", googlesearch_button)



time.sleep(10)
driver.quit()
