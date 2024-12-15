from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Находим модальное окно и закрываем его
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)
modal = driver.find_element(By.CSS_SELECTOR, "div.modal-footer > p")
modal.click()

# Выжидаем некоторое время, чтобы модальное окно успело закрыться
sleep(5)

driver.quit()
