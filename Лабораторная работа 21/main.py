import doctest

# TODO Написать 3 класса с документацией и аннотацией типов
class Pot:
    def __init__(self, wrap_status, liquid_status, liquid_capacity):
        """"
        Создание объекта класса "банка"
        :param wrap_status: статус банки (открыта или закрыта), задаётся латинскими буквами "C" или "O"
        :param liquid_status: текущее количество сока в банки
        :param liquid_capacity: вместимость банки
        Примеры:
        >>> my_pot = Pot(0, 30, 100)
        """


        if (wrap_status != 0) and (wrap_status != 1):
            raise ValueError("pot must be opened (0) or closed (1)")
        self.wrap_status = wrap_status
        if not isinstance(liquid_status, (int, float)):
            raise TypeError("Wrong type for liquid_status")
        if not isinstance(liquid_capacity, (int, float)):
            raise TypeError("Wrong type for liquid_capacity")
        if liquid_status > liquid_capacity:
            raise ValueError("Capacity must be graiter than occupied volume")
        if liquid_status < 0:
            raise ValueError("Amount of liquid must not be lesser than zero")
        if liquid_capacity < 0:
            raise ValueError("Amount of liquid must not be lesser than zero")
        self.liquid_status = liquid_status
        self.liquid_capacity = liquid_capacity
    def open_pot(self):
        """"
        Функция открывает банку, если та была закрыта,
        в случае успеха выводится сообщение (банка открыта).
        :raise ValueError: вызывает ошибку, если банка была открыта при вызове метода
        Примеры:
        >>> my_pot = Pot(1, 30, 100)
        >>> my_pot.open_pot()
        """
    ...
    def close_pot(self):
        """"
        Функция закрывает банку, если та была открыта,
        в случае успеха выводится сообщение (банка закрыта).
        :raise ValueError: вызывает ошибку, если бутылка была закрыта при вызове метода
        Примеры:
        >>> my_pot = Pot(0, 30, 100)
        >>> my_pot.close_pot()
        """
        ...
    def add_liquid(self, liquid_input):
        """"
        Функция добавляет сок в банку, если банка открыта
        :raise TypeErroe: вызывает ошибку при попытке налить не целое и не вещественное число сока
        :raise ValueError: вызывает ошибку при попытке переполнить банку или налить отрицательные значения
        :return: новое число занятого объёма банки
        примеры:
        >>> my_pot = Pot(0, 30, 100)
        >>> my_pot.add_liquid(50)
        """
        ...


class Truck:
    def __init__(self, truck_load_capacity, cargo_type):
        """
        Создание объекта класса грузовик:
        :param truck_load_capacity: грузоподъемность грузовика, тонны
        :param cargo_type: тип груза
        Примеры:
        >>> tank = Truck(40, "Petrol")
        """
        if not isinstance(truck_load_capacity, (int, float)):
            raise TypeError("Truck load capacity must be int or float")
        if truck_load_capacity <= 0:
            raise ValueError("Truck load capacity must be graiter than 0")
        if not isinstance(cargo_type, str):
            raise TypeError("Name of cargo type must be string")


    def check_load_capacity(self):
        """
        Метод смотрит рузоподъемность грузовика
        :return: возвращает значение рузоподъемности
        Примеры:
        >>> tank = Truck(100, "Petrol")
        >>> tank.check_load_capacity()
        """
    ...

    def check_is_cargo_type(self, type_):
        """
        Метод проверяет соответствие груза грузовика с предложенным пользователем типом
        :param type_: груз, с которым сравнивается значение
        :raise ErrorType: вызывает ошибку, если type_ не строковая переменная
        :return: возвращает значение True, если тип груза грузовика совпал с type_, False - если не совпал
        Примеры:
        >>> tank = Truck(100, "Petrol")
        >>> tank.check_is_cargo_type("Oil")
        """
        ...

class Country:
    def __init__(self, population, area):
        """
        Инициализация объекта город:
        :param population: население страны
        :param area: площадь страны (в квадратных километрах)
        Примеры:
        >>> china = Country(1411778, 9598962)
        """
        if not isinstance(population, int):
            raise TypeError("Population must be int!")
        if population <= 0:
            raise ValueError("Population must be graiter than 0")
        if not isinstance(area, (int, float)):
            raise TypeError("Area must be float or int!")
        if area <= 0:
            raise ValueError("Area must be graiter than 0")

    def population_census(self):
        """
        Метод проводит перепись населения
        :return: возвращает новое число населения
        Примеры:
        >>> china = Country(1411778, 9598962)
        >>> china.population_census()
        """
        ...

    def country_expand(self, additional_area):
        """
        Метод увеличивает площадь страны на additional_area
        :param additional_area: дополнительная площадь страны
        :raise TypeError: вызывает ошибку, если тип additional_area не int и не float
        :return: возвращает новую площадь города
        Примеры:
        >>> china = Country(1411778, 9598962)
        >>> china.country_expand(36197.0669)
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
    doctest.testmod()
