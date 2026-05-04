from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from google_homepage_test import driver

# Initialize the wait object with a 10-second timeout
wait = WebDriverWait(driver, 10)

try:
    # 1. Wait for the search box to be visible
    search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
    search_box.send_keys("Explicit Wait")

    # 2. Wait for the search button to be clickable
    # Note: Google's search button name is "btnK"
    googlesearch_button = wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
    googlesearch_button.click()

finally:
    print("Wait script execution finished.")
