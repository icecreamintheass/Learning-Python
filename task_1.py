class Animal:
    """Базовый класс для всех животных."""

    def __init__(self, name, age):
        """Создание животного с именем и возрастом."""
        self.name = name
        self.age = age

    def make_sound(self):
        """Метод, который должен быть переопределен в дочерних классах."""
        return "Какой-то звук"

    def __str__(self):
        """Строковое представление животного."""
        return f"{self.name}, возраст {self.age} лет."

    def __repr__(self):
        """Машинное представление объекта."""
        return f"Animal(name='{self.name}', age={self.age})"


class Cat(Animal):
    """Класс, представляющий кота."""

    def __init__(self, name, age, breed):
        """Создание кота с породой."""
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        """Кот мяукает, вместо общего звука."""
        return f"{self.name} говорит: Мяу!"

    def __str__(self):
        """Добавляем информацию о породе в описание кота."""
        return f"{self.name}, порода {self.breed}, возраст {self.age} лет."

    def __repr__(self):
        """Машинное представление кота."""
        return f"Cat(name='{self.name}', age={self.age}, breed='{self.breed}')"


if __name__ == "__main__":
    cat = Cat("Левик", 5, "Перс")
    print(cat)
    print(cat.make_sound())
    print(repr(cat))  # Проверка метода __repr__
