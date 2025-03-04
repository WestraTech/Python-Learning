class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def apply_discount(self, percent):
        discount = self.price * percent/100
        self.price -= discount

milk = Product("Milk", 2)
milk.apply_discount(10)

class Ebook(Product):
    def __init__(self, title, price, pages):
        super().__init__(title, price)
        self.pages = pages

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_products(self):
        return len(self.products)
    
    def subtotal(self):
        total = 0
        for product in self.products:
            total += product.price

        return total
    

cart = Cart()

cart.add_product(Product("Banana", 0.6))
cart.add_product(Product("Earbuds", 11.99))
cart.add_product(Ebook("Python", 2.99, 310))

print(cart.total_products())
