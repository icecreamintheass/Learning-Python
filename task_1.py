import doctest


class Car:
    def __init__(self, model: str, year: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param model: Модель автомобиля
        :param year: Год выпуска

        Примеры:
        >>> car = Car('Tesla', 2022)
        >>> car.model
        'Tesla'
        >>> car.year
        2022
        """
        self.model = model
        self.year = year

    def start_engine(self) -> None:
        """Запуск двигателя"""
        ...

    def stop_engine(self) -> None:
        """Остановка двигателя"""
        ...


class VK:
    def __init__(self, username: str, email: str):
        """
        Создание и подготовка к работе объекта "VK аккаунт"

        :param username: Имя пользователя
        :param email: Адрес электронной почты

        Примеры:
        >>> vk = VK('john_doe', 'john@example.com')
        >>> vk.username
        'john_doe'
        >>> vk.email
        'john@example.com'
        """
        self.username = username
        self.email = email

    def send_message(self, message: str) -> None:
        """Отправка сообщения"""
        ...

    @staticmethod
    def receive_message() -> str:
        """
        Получение сообщения. Так как это статический метод,
        он не зависит от экземпляра класса и не использует self.

        :return: Сообщение от системы

        Примеры:
        >>> VK.receive_message()
        'Hello!'
        """
        return "Hello!"


class Stack:
    def __init__(self):
        """
        Создание и подготовка к работе объекта "Стек"

        Примеры:
        >>> stack = Stack()
        >>> stack.push(5)
        >>> stack.pop()
        5
        """
        self.items = []

    def push(self, item: int) -> None:
        """Добавление элемента в стек"""
        self.items.append(item)

    def pop(self) -> int:
        """Удаление и возврат элемента из стека"""
        return self.items.pop()


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации