class User:
    def __init__(self, name, _age, __password):
        self.name = name
        self._age = _age
        self.__password = __password

    def get_info(self):
        return f"{self.name}"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            print("Yosh 0 dan kichik bo'lmasligi kerak")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) >= 6:
            self.__password = value
        else:
            print("Parol kamida 6 ta belgidan iborat bo'lishi kerak")

    def __str__(self):
        return f"Ism: {self.name}\nYosh: {self.age}"

    def __repr__(self):
        return f"User('{self.name}', {self.age}, '{self.password}')"


user1 = User("Ali", 20, "123456")
user2 = User("Vali", 25, "abcdef")

print(user1)
print(user2)

print(user1.age)
user1.age = 21
print(user1.age)

user2.age = -5
print(user2.age)

print(user1.password)
user1.password = "qwerty"
print(user1.password)

user2.password = "123"
print(user2.password)

print(repr(user1))
print(repr(user2))