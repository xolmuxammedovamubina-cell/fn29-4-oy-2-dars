class BankAccount:
    def __init__(self, owner, _balance, __card_number):
        self.owner = owner
        self._balance = _balance
        self.__card_number = __card_number

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            print("Balans 0 dan kichik bo'lmasligi kerak")

    def __str__(self):
        return f"Egasi: {self.owner}\nBalans: {self.balance}"

    def __repr__(self):
        return f"BankAccount('{self.owner}', {self.balance}, {self.__card_number})"


user1 = BankAccount("Ali", 2500000, 9876543210123456)
user2 = BankAccount("Vali", 2000000, 8765432101234567)

print(user1)
print(user2)

print(user1.balance)

user1.balance = 3000000
print(user1.balance)

user2.balance = -5
print(user2.balance)

print(user1.__card_number)