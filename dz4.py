class Product:
    def __init__(self, name="Семечки", quantity=4, price=18):
        self.name = name
        self.quantity = quantity
        self.price = price

    def calculate_total_price(self):
        return self.quantity * self.price

    def display_info(self):
        print(
            "Имя : " + self.name + "; количество: " + str(self.quantity) + "; цена за каждую пачку: " + str(self.price) + "; цена зa все: " + str(self.calculate_total_price()))


semechki = Product()
semechki.display_info()