from selenium import webdriver
from selenium.webdriver.common.by import By
from configuration import *

# Настройка драйвера браузера
driver = webdriver.Chrome()
driver.get(URL_3)

# Вход в аккаунт
username_field = driver.find_element(
    By.ID, "user-name").send_keys("standard_user")
password_field = driver.find_element(
    By.ID, "password").send_keys("secret_sauce")
login_button = driver.find_element(By.ID, "login-button").click()

# Добавление товаров в корзину
backpack_add_to_cart_button = driver.find_element(
    By.ID, "add-to-cart-sauce-labs-backpack").click()
t_shirt_add_to_cart_button = driver.find_element(
    By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
onesie_add_to_cart_button = driver.find_element(
    By.ID, "add-to-cart-sauce-labs-onesie").click()

# Переход в корзину
cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()

# Оформление заказа
checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()

# Заполнение формы
name_field = driver.find_element(By.ID, "first-name")
name_field.send_keys("Tamara")
surname_field = driver.find_element(By.ID, "last-name")
surname_field.send_keys("Chebotareva")
postal_code_field = driver.find_element(By.ID, "postal-code")
postal_code_field.send_keys("123456")
continue_button = driver.find_element(By.ID, "continue")
continue_button.click()

# Чтение итоговой стоимости
total_price_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
total_price = total_price_element.text
print("Итоговая стоимость:", total_price)

# Закрытие браузера
driver.quit()
