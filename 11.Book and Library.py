class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"«{self.title}» – {self.author} ({self.year})"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книгу '{book.title}' додано до бібліотеки '{self.name}'.")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def display_books(self):
        if not self.books:
            print("У бібліотеці немає книг.")
        else:
            print(f"Книги у бібліотеці '{self.name}':")
            for book in self.books:
                print("  ", book)

# Приклад використання:
if __name__ == "__main__":
    library = Library("Центральна бібліотека")
    book1 = Book("Тореадори з Васюківки", "Всеволод Нестайко", 1964)
    book2 = Book("Кобзар", "Тарас Шевченко", 1840)
    library.add_book(book1)
    library.add_book(book2)
    library.display_books()

    query = "Кобзар"
    found = library.find_book(query)
    if found:
        print(f"Знайдено книгу: {found}")
    else:
        print(f"Книгу '{query}' не знайдено в бібліотеці.")