from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

# Переходим на страницу
chrome.get('http://uitestingplayground.com/classattr')

# Находим синюю кнопку и нажимаем на нее
blue_button_chrome = chrome.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
blue_button_chrome.click()

sleep(3)

# нажимаем кнопку во всплывающем окне
chrome.switch_to.alert.accept()

sleep(3)
# закрываем браузер
chrome.quit()
