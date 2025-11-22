class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades  # список оцінок

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

# Створення об'єкта й демонстрація середнього балу
student = Student('Олександра', [12, 10, 11, 8, 12])
print(f"Середній бал студента {student.name}: {student.average_grade():.2f}")