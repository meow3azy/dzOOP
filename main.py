class Category:
    def __init__(self, name, products):
        self.name = name
        self.products = products

    def __str__(self):
        return f"{self.name}, количество продуктов: ? шт."

    def __iter__(self):
        return CategoryIterator(self)


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: Цена - {self.price} руб, Количество - {self.quantity} шт"


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


