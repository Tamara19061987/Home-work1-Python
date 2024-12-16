from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.ID, "newButtonName").send_keys('SkyPro')

button = driver.find_element(By.ID, "updatingButton").click()

button_name = driver.find_element(By.ID, "updatingButton").text

print(button_name)
