import random

class Unit:
    def __init__(self, name, attack_power=10):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

    def attack(self, other_unit):
        damage = self.attack_power
        other_unit.health -= damage
        print(f"{self.name} атакує {other_unit.name} і завдає {damage} шкоди!")
        if other_unit.health < 0:
            other_unit.health = 0

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}: здоров'я = {self.health}"

class Game:
    def __init__(self):
        self.player = Unit("Гравець", attack_power=random.randint(8, 12))
        self.enemy = Unit("Ворог", attack_power=random.randint(8, 12))

    def play(self):
        print("Гра почалася!")
        print(self.player)
        print(self.enemy)
        print("-" * 30)

        turn = 0
        while self.player.is_alive() and self.enemy.is_alive():
            turn += 1
            print(f"--- Хід {turn} ---")
            input("Натисніть Enter, щоб атакувати!")
            self.player.attack(self.enemy)
            print(self.enemy)

            if not self.enemy.is_alive():
                print(f"{self.enemy.name} переможений! Ви виграли!")
                break

            self.enemy.attack(self.player)
            print(self.player)

            if not self.player.is_alive():
                print(f"{self.player.name} переможений! Ви програли.")
                break
            print("-" * 30)

if __name__ == "__main__":
    game = Game()
    game.play()