from typing import Optional

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_  # Идентификатор книги
        self.name = name  # Название книги
        self.pages = pages  # Количество страниц в книге


class Library:
    def __init__(self, books = []) -> None:
        self.books = books

    def get_next_book_id(self) -> int:
        """Метод, который возвращает индентификатор для добавления новой книги в библиотеку"""
        if len(self.books) == 0:  # Если библиотека пустая, возвращаем 1
            return 1
        else:  # Если библиотека не пустая, возвращаем id последней книги, увеличенный на 1
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_) -> int:
        """Метод, который возвращает индекс книги в списке по запрашиваемому id"""
        for index, current_book in enumerate(self.books):  # Перебираем пары индекс-значение в списке книг
            if current_book.id_ == id_:  # Если id соответствует запрашиваемому, возвращаем индекс
                return index


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
