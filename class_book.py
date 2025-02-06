class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    book1 = Book(id_=1, name="test_name_1", pages=200)
    book2 = Book(id_=2, name="test_name_2", pages=400)

    print(book1)
    print(book2)

    print([book1,
           book2])