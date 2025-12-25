class Book:
    def __init__(self, title, autor, year):
        self.title = title
        self.autor = autor
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.autor}, Год издания: {self.year}"


CaP = Book("Мастер и Маргаита", "Михаил Афанасьевич Булгаков", 1928)
print(CaP.get_info())
