import pytest
from selenium.webdriver.common.by import By
from configuration import *


def test_data_types_form(chrome_browser):
    chrome_browser.get(URL_1)

    chrome_browser.find_element(By.NAME, "first-name").send_keys(first_name)
    chrome_browser.find_element(By.NAME, "last-name").send_keys(last_name)
    chrome_browser.find_element(By.NAME, "address").send_keys(address)
    chrome_browser.find_element(By.NAME, "zip-code").send_keys(zip_code)
    chrome_browser.find_element(By.NAME, "city").send_keys(city)
    chrome_browser.find_element(By.NAME, "country").send_keys(country)
    chrome_browser.find_element(By.NAME, "e-mail").send_keys(email)
    chrome_browser.find_element(By.NAME, "phone").send_keys(phone_number)
    chrome_browser.find_element(
        By.NAME, "job-position").send_keys(job_position)
    chrome_browser.find_element(By.NAME, "company").send_keys(company)

    chrome_browser.find_element(By.TAG_NAME, "button").click()

    assert "danger" in chrome_browser.find_element(
        By.ID, "zip-code").get_attribute("class")
    assert "success" in chrome_browser.find_element(
        By.ID, "first-name").get_attribute("class")
    assert "success" in chrome_browser.find_element(
        By.ID, "last-name").get_attribute("class")
    assert "success" in chrome_browser.find_element(
        By.ID, "address").get_attribute("class")
    assert "success" in chrome_browser.find_element(
        By.ID, "city").get_attribute("class")
    assert "success" in chrome_browser.find_element(
        By.ID, "country").get_attribute("class")
    assert "success" in chrome_browser.find_element(
        By.ID, "e-mail").get_attribute("class")
    assert "success" in chrome_browser.find_element(
        By.ID, "phone").get_attribute("class")
    assert "success" in chrome_browser.find_element(
        By.ID, "job-position").get_attribute("class")
    assert "success" in chrome_browser.find_element(
        By.ID, "company").get_attribute("class")
