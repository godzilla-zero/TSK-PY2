class Audiobook:
    def __init__(self, name: str, dur: int):
        """
        Создание объекта класса аудиокнига
        :param name: название аудиокниги
        :param dur: длительность аудиокниги (в минутах)

        Примеры:
        >>> test_audiobook = Audiobook("Портрет Дориана Грея", 654)  #Инициализация объекта класса
        """
        self.name = name  # Название аудиокниги можно менять, как и его тип (но не рекомендуется)
        self.duration = dur
        self._comm = None  # Комментарий к аудиокниги, по умолчанию отсутствует, для добавления применить метод add_comm
        self._accordance = None  # Параметр соответствия аудиокниги теме, по умолчанию отсутствует, добавляется методом


    def add_comm(self, message: str):
        """
        Метод, позволяющий оставить комментарий к аудиокниги
        :param message:
        :return:

        Примеры:
        >>> test_audiobook = Audiobook("Портрет Дориана Грея", 654)  #Инициализация объекта класса
        >>> test_audiobook.add_comm("Озвучка хорошая. Произведение замечательное")
        """
        self._comm = message

    def write_com(self):
        """
        Метод, позволяющий вернуть ранее оставленный комментарий к аудиокниги
        :return: возвращает комментарий
        Примеры:
        >>> test_audiobook = Audiobook("Портрет Дориана Грея", 654)  #Инициализация объекта класса
        >>> test_audiobook.add_comm("Озвучка хорошая. Произведение замечательное")
        >>> test_audiobook.write_com()
        'Озвучка хорошая. Произведение замечательное'
        """
        return self._comm

    def add_accordance(self, rating: float):
        """
        Метод, позволяющий добавить степень соответствия аудиокниги теме
        :param rating: степень соответствия аудиокниги теме (от 0 до 10)

        Примеры:
        >>> test_audiobook = Audiobook("Портрет Дориана Грея", 654)
        >>> test_audiobook.add_accordance(9.0)
        """

        if isinstance(rating, float):
            if 10.0 >= rating >= 0.0:
                self._accordance = rating
            else:
                raise ValueError("accordance must be from 0 to 10")
        else:
            raise TypeError("accordance must be float")

    def check_accordance(self):
        """
        Метод, печатающий степень соответствия аудиокниги теме. Предварительно необходимо добавить её к экземпляру класса
        Примеры:
        >>> test_audiobook = Audiobook("Портрет Дориана Грея", 654)
        >>> test_audiobook.add_accordance(9.0)
        >>> test_audiobook.check_accordance()
        Соответствие аудиокниги теме:9.0
        """
        print(f'Соответствие аудиокниги теме:{self._accordance}')


    @property
    def duration(self):
        """
        Геттер для атрибута (длительности) аудиокниги
        :param self:
        :return:
        """
        return self._duration

    @duration.setter  # Длительность аудиокниги должна быть положительным целым числом, поэтому создан атрибут
    def duration(self, dur: int):
        """
        Cеттер для атрибута (длительности) аудиокниги
        :param self:
        :param dur: длительность аудиокниги
        :return:
        """
        if isinstance(dur, int):
            if dur > 0:
                self._duration = dur
            else:
                raise ValueError(f'duration of audiobook must be greater than zero, while incoming {dur}')
        else:
            raise ValueError(f'audiobook duration must be int, while incoming is {type(dur)}')

    def __str__(self):
        """
        Магический метод __str__
        :return: Возвращает название и длительность аудиокниги

        Примеры:
        >>> test_audiobook = Audiobook("Портрет Дориана Грея", 654)
        >>> print(test_audiobook)
        Аудиокнига "Портрет Дориана Грея", длительность 654
        """
        return f'Аудиокнига "{self.name}", длительность {self.duration}'

    def __repr__(self):
        """
        Магический метод, выдающий строку, необходимую для инициализации аудиокниги
        :return:
        Примеры:
        >>> test_audiobook = Audiobook("Портрет Дориана Грея", 654)
        >>> repr(test_audiobook)
        "Audiobook(name='Портрет Дориана Грея', dur=654)"
        """
        return f"{self.__class__.__name__}(name={self.name!r}, dur={self.duration})"


class HistoricalAudiobook(Audiobook):
    def __init__(self, name: str, dur: int, century: str):
        """
        Создание объекта класса историческая аудиокнига
        :param name: название аудиокниги
        :param dur:  длительность аудиокниги
        :param century: век, события которого описывает аудиокнига (римские цифры)
        Примеры:
        >>> test_audiobook = HistoricalAudiobook("Московское царство", 2710 , "XVI") # инициализация объекта класса
        """
        super().__init__(name, dur)  # имя и длительность наследуются
        self.century = century
        self._comm = None
        self._accordance = None


    def __str__(self):  # Перегрузка необходима в связи с добавлением слова "исторический" и параметра (век)
        """
        Магический метод __str__
        :return: Возвращает название и длительность аудиокниги

        Примеры:
        >>> test_audiobook = HistoricalAudiobook("Московское царство", 2710 , "XVI")
        >>> print(test_audiobook)
        Историческая Аудиокнига "Московское царство", длительность 2710, XVI век
        """
        return f'Историческая Аудиокнига "{self.name}", длительность {self.duration}, {self.century} век'

    def __repr__(self):  # Перегрузка необходима ради введения в метод нового параметра (век)
        """
        Магический метод, выдающий строку, необходимую для инициализации исторической аудиокниги
        :return:
        Примеры:
        >>> test_audiobook = HistoricalAudiobook("Московское царство", 2710 , "XVI")
        >>> print(repr(test_audiobook))
        HistoricalAudiobook(name='Московское царство', dur=2710, century = XVI)
        """
        return f"{self.__class__.__name__}(name={self.name!r}, dur={self.duration}, century = {self.century})"

    def check_accordance(self):  # методу необходима перегрузка, чтобы показывать степень исторического соответствия
        """
        Метод, печатающий степень исторического соответствия аудиокниги, ранее добавленную
        методом add_accordance
        Примеры:
        >>> test_audiobook = HistoricalAudiobook("Московское царство", 2710 , "XVI")
        >>> test_audiobook.add_accordance(5.5)
        >>> test_audiobook.check_accordance()
        Степень исторического соответствия:5.5
        """
        print(f'Степень исторического соответствия:{self._accordance}')



if __name__ == "__main__":
    # Write your solution here
    """
    Унаследованы методы add_accordance, add_comm и write_comm. Метод check_accordance перегружен
    Возможные проверки на соответствие века формату цифр опущены, так как век может быть указан
    с модификатором до н.э или н.э.
    """
    pass
