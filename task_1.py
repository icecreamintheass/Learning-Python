class Book:
    def __init__(self, book_id, title, author_name):
        self.book_id = book_id
        self._title = title
        self._author_name = author_name

    @property
    def title(self):
        return self._title

    @property
    def author_name(self):
        return self._author_name

    def __str__(self):
        return f'Книга "{self.title}"'

    def __repr__(self):
        return f"Book(book_id={self.book_id}, title='{self.title}', author_name='{self.author_name}')"


class PaperBook(Book):
    def __init__(self, book_id, title, author_name, page_count):
        super().__init__(book_id, title, author_name)
        self._page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if value > 0:
            self._page_count = value
        else:
            raise ValueError("Количество страниц должно быть больше нуля.")

    def __repr__(self):
        return f"PaperBook(book_id={self.book_id}, title='{self.title}', author_name='{self.author_name}', page_count={self.page_count})"


class AudioBook(Book):
    def __init__(self, book_id, title, author_name, audio_duration):
        super().__init__(book_id, title, author_name)
        self._audio_duration = audio_duration

    @property
    def audio_duration(self):
        return self._audio_duration

    @audio_duration.setter
    def audio_duration(self, value):
        if value > 0:
            self._audio_duration = value
        else:
            raise ValueError("Продолжительность аудиокниги должна быть больше нуля.")

    def __repr__(self):
        return f"AudioBook(book_id={self.book_id}, title='{self.title}', author_name='{self.author_name}', audio_duration={self.audio_duration})"


if __name__ == '__main__':
    paper_book = PaperBook(1, "Марсианские хроники", "Рэй Брэдбери", 288)
    audio_book = AudioBook(2, "Цветы для Элджернона", "Дэниел Киз", 12.5)

    # Вывод информации о книгах
    print(paper_book)  # Книга "Марсианские хроники"
    print(audio_book)  # Книга "Цветы для Элджернона"

    print(repr(paper_book))  # PaperBook(book_id=1, title='Марсианские хроники', author_name='Рэй Брэдбери', page_count=288)
    print(repr(audio_book))  # AudioBook(book_id=2, title='Цветы для Элджернона', author_name='Дэниел Киз', audio_duration=12.5)

    # Изменение параметров книги
    paper_book.page_count = 300
    audio_book.audio_duration = 13.0
    print(paper_book.page_count)  # 300
    print(audio_book.audio_duration)  # 13.0
