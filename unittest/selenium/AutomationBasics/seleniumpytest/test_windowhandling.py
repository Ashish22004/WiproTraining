import time

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # Setup: Initialize the Edge driver
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://the-internet.herokuapp.com')

    yield driver  # This provides the driver to your test functions

    # Teardown: Close the browser after the test finishes
    driver.quit()

    time.sleep(3)


# Example test case using the fixture
def test_example_window(driver):
    assert "The Internet" in driver.title
