import requests
from datetime import datetime
from bs4 import BeautifulSoup

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
    
    def get_hourly_weather(self):
        """
        Функцмя для получения списка в формате: 
        [дата, время, температура, как ощущается, погода, вероятность дождя(в %)]
        """
        response = requests.get(self.__url)
        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'html.parser')
        info = soup.find_all('li', class_='AppHourlyItem_container__aqC1z')

        dt = datetime.now()
        date = dt.strftime("%d.%m.%Y")

        if info:
            with open("test.txt", "w", encoding="utf-8") as f:
                for i in info:
                    data = i.find('p', class_="A11Y_visuallyHidden__y0sw0 visuallyHidden").text.strip()

                    if not data[0].isdigit():
                        f.write(data + f"\n")
                        continue

                    time = data[0:5]
                    print(time)

                    f.write(data + f"\n")

                    #f.write([date, temperature, apparent_temperature, weather, probability_of_rain])


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