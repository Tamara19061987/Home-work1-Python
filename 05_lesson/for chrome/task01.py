from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

# Переходим на страницу
chrome.get('http://the-internet.herokuapp.com/add_remove_elements/')

# Добавляем элементы 5 раз
for i in range(5):
    # Находим кнопку Add Element и нажимаем на нее
    add_button = chrome.find_element(
        By.XPATH, '//button[text()="Add Element"]')
    add_button.click()

sleep(5)

# Собираем список кнопок Delete
delete_buttons_chrome = chrome.find_elements(
    By.XPATH, '//button[text()="Delete"]')

# Выводим размер списка
print("Размер списка кнопок Delete:", len(delete_buttons_chrome))

# Закрываем браузер
chrome.quit()
