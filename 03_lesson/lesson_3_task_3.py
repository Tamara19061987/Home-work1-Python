from address import Address 
from mailing import Mailing

# Пример создания объекта класса Mailing
my_address_to = Address("685030", "Магадан", "Пролетарская улица", "108", "155")
my_address_from = Address("630047", "Новосибирск", "улица Залесского", "12", "6")
my_mailing = Mailing(my_address_to, my_address_from, 100, "1234567890")

# Вывод информации об отправлении
print(f"Отправление {my_mailing.track} из {my_address_to.index}, {my_address_to.city}, {my_address_to.street}, {my_address_to.house} - {my_address_to.apartment} в {my_address_from.index}, {my_address_from.city}, {my_address_from.street}, {my_address_from.house} - {my_address_from.apartment}. Стоимость {my_mailing.cost} рублей.")