import doctest

if __name__ == "__main__":
    # Write your solution here
    doctest.testmod()
    pass
class Game:
    """ Базовый класс игры.
    test_game = Game("brawl_stars", 9)"""
    def __init__(self, name: str, age_rating: int):
        self.level = None
        self.storage = None
        self.name = name
        self.age_rating = age_rating


    def game_storage(self, storage: int):
        """ Метод, позволяющий определить сколько памяти необходимо для игры.
        test_game = Game("brawl_stars", 9)
        test_game.game_storage(10)
        Память игры 10"""
        self.storage = storage
        return f'Память игры "{self.storage}"'

    def game_difficulty(self, level: str):
        """ Метод, позволяющий определить уровень сложности игры.
        test_game = Game("brawl_stars", 9)
        test_game.game_difficulty(easy)
        Сложность игры easy"""
        self.level = level
        return f'Сложность игры "{self.level}"'


    def __str__(self):
        return f"Игра {self.name}. Возрастное ограничение {self.age_rating}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, age_rating={self.age_rating!r})"


class Mobile_Game(Game):
    """ Дочерний класс мобильной игры. """
    def __init__(self, name: str, age_rating: int):
        self.name = name
        self.age_rating = age_rating


    def __str__(self):
        return f"Игра {self.name}. Возрастное ограничение {self.age_rating}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, age_rating={self.age_rating!r})"

    def game_storage(self, storage: int):
        """ Метод, позволяющий определить сколько памяти необходимо для игры. Метод переопределен, тк важно,
        что это именно мобильная игра """
        self.storage = storage
        return f'Память мобильной игры "{self.storage}"'

    def game_difficulty(self, level: str):
        """ Метод, позволяющий определить уровень сложности игры. """
        self.level = level
        return f'Сложность игры "{self.level}"'

