class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Внесено: {amount} грн.")
        else:
            print("Сума повинна бути більше нуля!")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Недостатньо коштів на рахунку!")
        elif amount <= 0:
            print("Сума повинна бути більше нуля!")
        else:
            self._balance -= amount
            print(f"Знято: {amount} грн.")

    def get_balance(self):
        return self._balance

# Приклад використання:
account = BankAccount(500)
account.deposit(250)
account.withdraw(100)
account.withdraw(800) # Недостатньо коштів
print("Поточний баланс:", account.get_balance())