from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79161234567"),
    Smartphone("Samsung", "Galaxy S21", "+79162345678"),
    Smartphone("Google", "Pixel 6", "+79163456789"),
    Smartphone("OnePlus", "9 Pro", "+79164567890"),
    Smartphone("Xiaomi", "Mi 11", "+79165678901")
]

for item in catalog:
    print(item.brand + " - " + item.model + ": " + item.phone_number)