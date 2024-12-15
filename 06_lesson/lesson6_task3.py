from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ждём загрузки всех картинок
wait = WebDriverWait(driver, 20)
wait.until(EC.visibility_of_element_located((By.ID, "award")))

# Получаем атрибут src третьей картинки
third_img = driver.find_element(By.ID, "award")
src_attr = third_img.get_attribute("src")

# Выводим значение в консоль
print(src_attr)

driver.quit()