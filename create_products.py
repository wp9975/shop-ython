import random
from myshop import db, app
from myshop.models import Product

# Lista nazw produktów
product_names = [
    "Smartphone", "Laptop", "Smart TV", "Camera", "Headphones", 
    "Speaker", "Printer", "Desktop PC", "Tablet", "Game Console",
    "Keyboard", "Mouse", "Monitor", "External Hard Drive", "USB Flash Drive",
    "Webcam", "Smart Watch", "Bluetooth Earbuds", "Charger", "HDMI Cable"
]

# Tworzenie nowych produktów
with app.app_context():
    for name in product_names:
        description = f"This is a(n) {name}"
        price = round(random.uniform(50.0, 500.0), 2)  # losowa cena między 50 a 500
        product = Product(name=name, description=description, price=price)

        # Dodawanie produktu do sesji
        db.session.add(product)

    # Zatwierdzanie sesji, aby zapisać zmiany w bazie danych
    db.session.commit()
