import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://testpages.eviltester.com/pages/basics/alerts-javascript/')
    yield driver
    driver.quit()


# 1. SIMPLE ALERT TEST
def test_simple_js_alert(driver):
    driver.find_element(By.ID, "alertexamples").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am an alert box!"
    time.sleep(1)
    alert.accept()

    result = driver.find_element(By.ID, "alertexplanation").text
    assert "You triggered and handled the alert" in result


# 2. CONFIRM BOX - DISMISS (CANCEL)
def test_js_confirm_dismiss(driver):
    driver.find_element(By.ID, "confirmexample").click()
    alert = driver.switch_to.alert
    time.sleep(1)
    alert.dismiss()  # Clicks Cancel

    result = driver.find_element(By.ID, "confirmexplanation").text
    assert "You clicked Cancel" in result


# 3. CONFIRM BOX - ACCEPT (OK) -> Returns "true"
def test_js_confirm_accept(driver):
    driver.find_element(By.ID, "confirmexample").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a confirm alert"
    time.sleep(1)
    alert.accept()  # Clicks OK

    result = driver.find_element(By.ID, "confirmexplanation").text
    # This matches the result: "You clicked OK, confirm returned true."
    assert "confirm returned true" in result


# 4. PROMPT BOX TEST
def test_js_prompt(driver):
    driver.find_element(By.ID, "promptexample").click()
    alert = driver.switch_to.alert

    input_text = "change me"
    alert.send_keys(input_text)
    time.sleep(1)
    alert.accept()

    result = driver.find_element(By.ID, "promptexplanation").text
    assert f"returned {input_text}" in result
