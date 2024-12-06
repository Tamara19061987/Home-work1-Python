from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")

# Введите имя пользователя
username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("tomsmith")

# Введите пароль
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("SuperSecretPassword!")

sleep(3)

# Нажмите кнопку Login
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

sleep(3)

driver.quit()
