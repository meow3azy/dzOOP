
from main import Category
from main import Product

products = [
    Product("Яблоко", 100, 10),
    Product("Киви", 200, 2),
    Product("Бананы", 150, 5),
    Product("Молоко", 120, 8),
    Product("Шампунь", 300, 3)
]
category = Category("Список", products)
total_products = sum(product.quantity for product in category.products)

print(f"{category.name}, количество продуктов: {total_products} шт.")

a = Product("Бананы", 100, 10)
b = Product("Яблоко", 200, 2)

total_quantity = a.quantity + b.quantity

print("Общее количество продуктов:", total_quantity)

if __name__ == "__main__":
    products = [Product("Конфеты", 100, 10), Product("Печенье", 200, 2)]
    category = Category("Название категории", products)

    for product in category:
        print(product)
