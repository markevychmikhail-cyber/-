class FootballPlayer:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name} — {self.position}"

# Створюємо 11 футболістів
players = [
    FootballPlayer("Анатолій Трубін", "Воротар"),
    FootballPlayer("Віктор Корнієнко", "Захисник"),
    FootballPlayer("Микола Матвієнко", "Захисник"),
    FootballPlayer("Валерій Бондар", "Захисник"),
    FootballPlayer("Додо", "Захисник"),
    FootballPlayer("Тарас Степаненко", "Півзахисник"),
    FootballPlayer("Михаїл Мудрик", "Півзахисник"),
    FootballPlayer("Манор Соломон", "Півзахисник"),
    FootballPlayer("Марлос", "Півзахисник"),
    FootballPlayer("Лассіна Траоре", "Нападник"),
    FootballPlayer("Данило Сікан", "Нападник"),
]

# Виводимо склад команди
print("Склад команди:")
for player in players:
    print(player)