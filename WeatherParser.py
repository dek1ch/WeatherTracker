import re
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

class YandexWeatherParser:
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
        output = list()
        days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]

        response = requests.get(self.__url)
        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'html.parser')
        information_list = soup.find_all('li', class_='AppHourlyItem_container__aqC1z')

        date = datetime.now()

        prev_hour = date.hour
        is_nextDay = False

        if information_list:
            for i in information_list:
                data = i.find('p', class_="A11Y_visuallyHidden__y0sw0 visuallyHidden").text.strip()

                # Разбиение строки с погодой на данные с помощью регулярных выражений
                today = re.search(r'[а-я]+,', data) #Для контроял даты
                hour = re.search(r'\d\d:\d\d', data) #Час прогноза погоды
                temperature = re.search(r'[+-]\d{1,3}°,', data) #Температура
                apparent_temperature = re.search(r'как [+-]\d{1,3}°', data) #Какая температура будет ощущаться
                weather = re.search(r', [а-я ]+,', data) #Погода
                probability_of_rain = re.search(r'\d{1,2}%', data) #Вероятность дождя(если тот будет)

                if today and today.group()[:-1] in days:
                    prev_hour = 0
                    is_nextDay = True
                    date += timedelta(days=1)

                if (int(hour.group()[0:2]) - prev_hour) < 0 and is_nextDay : break
                prev_hour = int(hour.group()[0:2])

                if weather:
                    output.append([date.strftime("%d.%m.%Y"), hour.group(), temperature.group()[:-1], apparent_temperature.group()[4:], weather.group()[2:-1], probability_of_rain.group() if probability_of_rain else None])
        return output if output else None

    def updatePos(self):
        """
        Функция обновления ссылки для парсинга
        """
        self.__url = f"https://yandex.ru/pogoda/ru/moscow?lat={self.__latitude}&lon={self.__longitude}"
        print(self.__url)

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