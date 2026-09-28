class BankAccount:
    def __init__(self, owner, card_number, pin, balance, ):
        self.owner = owner
        self.card_number = card_number
        self.__pin = pin
        self.__balance = balance

    def show_info(self):
        return f"Mijozning ismi: {self.owner}\nKarta raqami: {self.card_number}\n"
    
    def check_balance(self, pin):
        if pin == self.__pin:
            return f"Balansi: {self.__balance}\n"
        else:
            print("Pin noto'g'ri. Pinni to'g'ri kiriting.\n")
    def deposit(self, amount):
        self.__balance += amount
        return f"Balansga pul qo'shildi.\nBalansi: {self.__balance}\n"
    def withdraw(self, amount, pin):
        if self.__pin == pin:
            self.__balance - amount
            return f"Pul yechib olindi.\nQoldi: {self.__balance}\n"
        else:
            return f"Pin noto'g'ri\n"
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return f"Pin o'zgartirildi\n"
        else:
            return f"Eski Pin noto'g'ri\n"


account = BankAccount("Ali", "8600 1234 5678 9012", 1234, 500000)

print(account.show_info())
print(account.check_balance(1234))
print(account.deposit(100000))
print(account.withdraw(200000, 1234))
print(account.change_pin(1234, 2008))
