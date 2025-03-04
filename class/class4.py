class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def apply_discount(self, percent):
        discount = self.price * percent/100
        self.price -= discount

milk = Product("Milk", 2)
milk.apply_discount(10)

print(milk.price)

class Ebook(Product):
    def __init__(self, title, price, pages):
        super().__init__(title, price)
        self.pages = pages

book = Ebook("Python", 2.99, 674)

book.apply_discount(50)

print(book.price)