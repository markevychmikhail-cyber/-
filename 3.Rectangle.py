class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Створення об'єкта та виведення площі
rect = Rectangle(5, 3)
print("Площа прямокутника:", rect.area())