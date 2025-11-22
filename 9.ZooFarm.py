import random

class Pet:
    def __init__(self, name, hunger=0, boredom=0):
        self._name = name
        self.hunger = hunger
        self.boredom = boredom

    def _pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "непогано"
        elif 11 <= unhappiness <= 15:
            m = "не сказати щоб добре"
        else:
            m = "жахливо"
        return m

    def talk(self):
        print(f"Мене звати {self._name}, і зараз я почуваюся {self.mood}")
        self._pass_time()

    def eat(self, food=4):
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self._pass_time()

    def play(self, fun=4):
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self._pass_time()

def main():
    print("Ласкаво просимо на зооферму!")
    num_pets = int(input("Скільки звіряток створити? "))
    pets = []
    for i in range(num_pets):
        name = input(f"Введіть ім'я для звірятка #{i+1}: ")
        hunger = random.randint(0, 10)
        boredom = random.randint(0, 10)
        pet = Pet(name, hunger, boredom)
        pets.append(pet)
        print(f"Створено звірятко {name}, голод: {hunger}, нудьга: {boredom}")

    choice = None
    while choice != "0":
        print("""
Зооферма

0 - Вийти
1 - Дізнатися про самопочуття всіх звіряток
2 - Погодувати всіх
3 - Пограти з усіма
""")
        choice = input("Ваш вибір: ")
        print()
        if choice == "0":
            print("До побачення.")
        elif choice == "1":
            for pet in pets:
                pet.talk()
        elif choice == "2":
            try:
                food_amount = int(input("Скільки одиниць їжі дати кожному звірятку? (1 і більше): "))
                if food_amount < 1:
                    print("Кількість їжі має бути більше 0.")
                else:
                    for pet in pets:
                        pet.eat(food=food_amount)
                    print("Всі звірятка нагодовані!")
            except ValueError:
                print("Введіть коректне число!")
        elif choice == "3":
            try:
                play_time = int(input("Скільки одиниць часу пограти з кожним звірятком? (1 і більше): "))
                if play_time < 1:
                    print("Час для гри має бути більше 0.")
                else:
                    for pet in pets:
                        pet.play(fun=play_time)
                    print("Всі звірятка повеселішали!")
            except ValueError:
                print("Введіть коректне число!")
        else:
            print("Вибачте, у мене немає пункту", choice)

if __name__ == "__main__":
    main()