import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")


#  TEXT INPUT
text_input = driver.find_element(By.ID, "my-text-id")
text_input.clear()
text_input.send_keys("Selenium WebDriver Demo")

#Password Input
password_input = driver.find_element(By.NAME, "my-password")
password_input.clear()
password_input.send_keys("secret123")

# Text area
textarea = driver.find_element(By.NAME, "my-textarea")
textarea.clear()
textarea.send_keys("This is a sample message")

# checkbox
checkbox = driver.find_element(By.ID, "my-check-2")
checkbox.click()

#radio button
radio = driver.find_element(By.ID, "my-radio-2")
radio.click()

#drop down
dropdown = driver.find_element(By.NAME, "my-select")
dropdown.click()

# CSS Selector with space
option = driver.find_element(By.CSS_SELECTOR, "select[name='my-select'] option[value='2']")
option.click()

# Datalist (corrected name from 'my-details' to 'my-datalist')
datalist_input = driver.find_element(By.NAME, "my-datalist")
datalist_input.send_keys("New York")


time.sleep(5)
driver.quit()
