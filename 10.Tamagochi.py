import random

class Pet:
    def __init__(self, name, hunger=0, boredom=0):
        self._name = name
        self.hunger = hunger
        self.boredom = boredom
        self.age = 1
        self.alive = True

    def _pass_time(self):
        # Вік підвищується повільно з кожною дією
        self.hunger += 1
        self.boredom += 1
        # Перевірка на смерть
        if self.hunger > 15 or self.boredom > 15:
            self.alive = False

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
        if self.alive:
            print(f"Мене звати {self._name}, мені {self.age} років, і зараз я почуваюся {self.mood}")
            self._pass_time()
        else:
            print(f"{self._name} помер! 😭")
    
    def eat(self, food=4):
        if self.alive:
            print("Мррр... Дякую!")
            self.hunger -= food
            if self.hunger < 0:
                self.hunger = 0
            self._pass_time()
        else:
            print(f"{self._name} помер! Годування більше не допоможе.")
    
    def play(self, fun=4):
        if self.alive:
            print("Yiii!")
            self.boredom -= fun
            if self.boredom < 0:
                self.boredom = 0
            self.age += 1  # Під час гри вік збільшується
            self._pass_time()
        else:
            print(f"{self._name} помер! Грати з ним більше не можна.")

def main():
    pet_name = input("Як ви назвете своє звірятко?: ")
    hunger = random.randint(0, 5)
    boredom = random.randint(0, 5)
    pet = Pet(pet_name, hunger, boredom)

    choice = None
    while choice != "0":
        print("""
Тамагочі

0 - Вийти
1 - Дізнатися про самопочуття звірятка
2 - Годувати звірятко
3 - Пограти зі звірятком
""")
        choice = input("Ваш вибір: ")
        print()
        if choice == "0":
            print("До побачення.")
        elif choice == "1":
            pet.talk()
        elif choice == "2":
            try:
                food_amount = int(input("Скільки одиниць їжі згодувати звірятку? (1 і більше): "))
                if food_amount < 1:
                    print("Кількість їжі має бути більше 0.")
                else:
                    pet.eat(food=food_amount)
            except ValueError:
                print("Введіть коректне число!")
        elif choice == "3":
            try:
                play_time = int(input("Скільки одиниць часу витратити на гру? (1 і більше): "))
                if play_time < 1:
                    print("Час для гри має бути більше 0.")
                else:
                    pet.play(fun=play_time)
            except ValueError:
                print("Введіть коректне число!")
        else:
            print("Вибачте, у мене немає пункту", choice)

        # Перевірка на смерть після дії користувача
        if not pet.alive:
            print(f"Ваше звірятко, {pet._name}, померло... Гра завершена.")
            break

if __name__ == "__main__":
    main()