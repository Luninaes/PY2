# TODO Написать 3 класса с документацией и аннотацией типов

class Car:
    def __init__(self, colour: str, price: int):
        self.colour = colour  # цвет машины
        self.price = price  # стоимость машины
        if not isinstance(colour, str):  # проверяем, что цвет типа str
            raise TypeError("Цвет должен быть типа str")  # вызываем ошибку
        if not isinstance(price, int):  # проверяем, что цена типа int
            raise TypeError("Цена должна быть типа int")
        if price < 0:                  # проверяем, что >0
            raise ValueError("Цена должна быть положительным числом")
    def turn_on(self):
         print("Двигатель включен") #Машина поехала
    def turn_off(self):
         print("Двигатель выключен") #Машина остановилась


class Flowers:
    def __init__(self, types: str, number_of_petals: int):
        self.types = types  # вид цветка
        self.number_of_petals = number_of_petals  # количество лепестков в цветке
        if not isinstance(types, str):  # проверяем, что вид типа str
            raise TypeError("Вид должен быть типа str")  # вызываем ошибку
        if not isinstance(number_of_petals, int):  # проверяем, что количество лепестков типа int
            raise TypeError("Количество лепестков должно быть типа int")
        if number_of_petals < 0:                  # проверяем, что >0
            raise ValueError("Кто-то сорвал все лепестки!")



    def wish(self, number_of_petals: int): # Считает четное ли количество лепестков
         if (number_of_petals % 2 == 0):
             print("Невезение!")
         else:
             print("Все сбудется!")


    def shop(self, types: str):
         """
         Проверяет есть ли такой цветок в магазине
         :return: Есть цветок в магазине или нет
         """
         ...
class Chocolate:
    def __init__(self, bag_length: int, chocolate_length: int):
        self.bag_length = bag_length  # длина сумки
        self.chocolate_length = chocolate_length  # длина шоколадки
        if not isinstance(bag_length, int):  # проверяем, что длина сумки типа int
            raise TypeError("Длина должна быть типа int")  # вызываем ошибку
        if not isinstance(chocolate_length, int):  # проверяем, что длина шоколадки типа int
            raise TypeError("Длина должна быть типа int")
        if chocolate_length > bag_length:       # проверяем, поместится ли шоколадка в сумку
            raise ValueError("Шоколадка не поместится в сумку!")



    def puzzle(self, bag_length: int, chocolate_length: int):
         number = bag_length / chocolate_length
         print(number) #Количество шоколадок


    def eat(self):

         print("Больше нет шоколадки!") # Съедаем шоколадку

if __name__ == "__main__":
    car = Car('blue', 1000000)
    flower = Flowers('sunflower', 17)
    chocolate = Chocolate(10, 2)
    import doctest
    doctest.testmod()
    pass
    # TODO работоспособность экземпляров класса проверить с помощью doctest
