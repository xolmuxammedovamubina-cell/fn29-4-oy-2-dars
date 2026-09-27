class Product:
    def __init__(self, name, _category, __price):
        self.name = name
        self._category = _category
        self.__price = __price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            print("Price 0 dan kichik bo'lmasligi kerak")

    def __str__(self):
        return f"Mahsulot: {self.name}\nNarxi: {self.price}"

    def __repr__(self):
        return f"Product('{self.name}', '{self._category}', {self.__price})"


product1 = Product("Telefon", "Elektronika", 5000000)
product2 = Product("Kitob", "Kitoblar", 50000)
product3 = Product("Sumka", "Aksessuar", 150000)

print(product1)
print(product2)
print(product3)

print(product1.price)

product1.price = 5500000
print(product1.price)

product2.price = -5000
print(product2.price)

product1.name = "iPhone"
print(product1.name)

print(repr(product1))
print(repr(product2))
print(repr(product3))