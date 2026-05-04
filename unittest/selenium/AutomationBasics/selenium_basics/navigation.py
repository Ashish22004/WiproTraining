import time
from google_homepage_test import driver

# 1. Navigate to a new site
driver.get("https://selenium.dev")
print(f"Current Title: {driver.title}")

# 2. Go back to the previous page (Google)
driver.back()
print("Navigated back to Google")

# 3. Go forward again (Selenium.dev)
driver.forward()
print("Navigated forward to Selenium.dev")

# 4. Refresh the current page
driver.refresh()
print("Page refreshed")

# Small delay to see the result before closing
time.sleep(3)
driver.quit()
