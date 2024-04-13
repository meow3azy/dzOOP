class Category:
    def __init__(self, name, products):
        self.name = name
        self.products = products

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.products)} шт."

    def __iter__(self):
        return CategoryIterator(self)


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: Цена - {self.price} руб, Количество - {self.quantity} шт"

    def __add__(self, other):
        if isinstance(other, Product) and self.name == other.name and self.price == other.price:
            return Product(self.name, self.price, self.quantity + other.quantity)
        return NotImplemented


class CategoryIterator:
    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.products):
            product = self.category.products[self.index]
            self.index += 1
            return product
        raise StopIteration
