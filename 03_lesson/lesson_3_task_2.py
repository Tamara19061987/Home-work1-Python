from smartphone import Smartphone

# Создание списка из пяти объектов Smartphone
catalog = [
 Smartphone("Vivo", "X100 Pro", "+79999999991"),
 Smartphone("Samsung", "Galaxy S24 Ultra", "+79999999992"),
 Smartphone("Apple", "iPhone 15 Pro Max", "+79999999993"),
 Smartphone("Huawei", "Mate 50 Pro", "+79999999994"),
 Smartphone("Motorola", "Edge 40 Pro", "+79999999995")
]

# Цикл для вывода информации о каждом объекте в списке
for item in catalog:
 print(f"{item.phone_brand} - {item.phone_model}. {item.phone_number}")
