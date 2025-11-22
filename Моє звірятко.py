# Моє звірятко
class Pet:
    """Віртуальний вихованець"""
    total = 0

    @staticmethod
    def status():
        print("Загальна кількість звірят", Pet.total)

    def __init__(self, name, hunger=0, boredom=0):
        Pet.total += 1
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

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Ім'я звірятка не може бути порожнім рядком.")
        else:
            self._name = new_name
            print("Ім'я успішно змінено.")

    def talk(self):
        print("Мене звати", self.name, 
              ", і зараз я почуваюся", self.mood)
        self._pass_time()

    def eat(self, food=4):
        print("Мррр... Дякую!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self._pass_time()

    def play(self, fun=4):
        print("Yiii!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self._pass_time()

def main():
    pet_name = input("Як ви назвете своє звірятко?: ")
    pet = Pet(pet_name)

    choice = None
    while choice != "0":
        print(
            """
Моє звірятко

0 - Вийти
1 - Дізнатися про самопочуття звірятка
2 - Годувати звірятко
3 - Пограти зі звірятком
"""
        )
        choice = input("Ваш вибір: ")
        print()
        
        # вихід
        if choice == "0":
            print("До побачення.")
        
        # бесіда зі звірятком
        elif choice == "1":
            pet.talk()
        
        # годування звірятка
        elif choice == "2":
            try:
                food_amount = int(input("Скільки одиниць їжі згодувати звірятку? (1 і більше): "))
                if food_amount < 1:
                    print("Кількість їжі має бути більше 0.")
                else:
                    pet.eat(food=food_amount)
            except ValueError:
                print("Введіть коректне число!")

        # гра зі звірятком
        elif choice == "3":
            try:
                play_time = int(input("Скільки одиниць часу витратити на гру? (1 і більше): "))
                if play_time < 1:
                    print("Час для гри має бути більше 0.")
                else:
                    pet.play(fun=play_time)
            except ValueError:
                print("Введіть коректне число!")
        
        # незрозуміле введення користувача
        else:
            print("Вибачте, у мене немає пункту", choice)

main()