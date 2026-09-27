class Employee:
    def __init__(self, name, _salary, __employee_id):
        self.name = name
        self._salary = _salary
        self.__employee_id = __employee_id

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self._salary = value
        else:
            print("Maosh 0 dan kichik bo'lmasligi kerak")

    def __str__(self):
        return f"Ism: {self.name}\nMaosh: {self.salary}"

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, {self.__employee_id})"


user1 = Employee("Ali", 2500000, 1)
user2 = Employee("Vali", 2000000, 2)
user3 = Employee("G'ani", 2100000, 3)

print(user1)
print(user2)
print(user3)

print(user1.salary)
user1.salary = 3000000
print(user1.salary)

user2.salary = -5
print(user2.salary)

print(user1.__employee_id)