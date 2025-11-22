class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self._speed = 0  # умовно-закритий атрибут

    def accelerate(self):
        self._speed += 5

    def brake(self):
        self._speed -= 5
        if self._speed < 0:
            self._speed = 0

    def display_info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Рік: {self.year}, Швидкість: {self._speed} км/год")

# Приклад використання:
car = Car("Toyota", "Camry", 2020)
car.display_info()      # Марка: Toyota, Модель: Camry, Рік: 2020, Швидкість: 0 км/год
car.accelerate()
car.display_info()      # Швидкість: 5 км/год
car.accelerate()
car.display_info()      # Швидкість: 10 км/год
car.brake()
car.display_info()      # Швидкість: 5 км/год
car.brake()
car.brake()
car.display_info()      # Швидкість: 0 км/год (не від'ємна)