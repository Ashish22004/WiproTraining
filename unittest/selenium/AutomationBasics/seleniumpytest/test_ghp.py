import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.google.com')
    yield driver
    driver.quit()


def test_ghpload(driver):
    pagetitle = driver.title
    assert pagetitle == 'Google', 'Google Home Page Not Loaded'


def test_imagespageload(driver):
    driver.find_element(By.LINK_TEXT, 'Images').click()
    # Wait for title to change to "Google Images"
    WebDriverWait(driver, 10).until(EC.title_is("Google Images"))
    pagetitle = driver.title
    assert pagetitle == 'Google Images', 'Images Page Not Loaded'


def test_businesslink(driver):
    driver.find_element(By.LINK_TEXT, 'Business').click()
    # Wait for the title to contain "Business" instead of time.sleep(1)
    WebDriverWait(driver, 10).until(EC.title_contains("Business"))

    assert 'Business' in driver.title, 'Business Page Not Loaded - Title check'
    assert 'business' in driver.current_url, 'Business Page Not Loaded - URL check'
