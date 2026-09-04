class WeatherParser:
    """
    Класс для получения погоды с сервиса Яндекс погоды
    """

    #=================================|Конструктор|=================================
    def __init__(self, latitude = 55.79, longitude = 37.595556):
        """
        Конструктор класса WeatherParser

        Args:
            latitude: Широта
            longitude: Долгота
        """
        self.__longitude = longitude
        self.__latitude = latitude
        self.updatePos()
    #===============================================================================
    


    def updatePos(self):
        """
        Функция обновления ссылки для парсинга
        """
        self.__url = f"https://yandex.ru/pogoda/ru/moscow?lat={self.__latitude}&lon={self.__longitude}"

    def setPosition(self, x: float, y: float):
        """
        Сеттер позиции, где будет проверяться погода

        Args:
            y: Широта
            x: Долгота
        """
        self.__longitude = x
        self.__latitude = y
        self.updatePos()
        
    def getPosition(self) -> list:
        """
        Геттер позиции, где проверяется погода
        """
        return [self.__longitude, self.__latitude]