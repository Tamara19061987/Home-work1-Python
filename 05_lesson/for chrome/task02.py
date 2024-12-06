from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


chrome = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

# Переходим на страницу
chrome.get('http://uitestingplayground.com/dynamicid')

# Находим синюю кнопку и нажимаем на нее
blue_button_chrome = chrome.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

# Закрываем браузер
chrome.quit()
