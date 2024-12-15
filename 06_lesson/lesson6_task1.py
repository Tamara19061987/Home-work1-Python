from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")

# Нажмите на синюю кнопку
button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# Подождите, пока появится зелёная плашка
wait = WebDriverWait(driver, 20)
green_box = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, '.bg-success')))

# Получите текст из зелёной плашки
element = driver.find_element(By.CSS_SELECTOR, '.bg-success')
text = element.text
print(text)

driver.quit()
