from WeatherParser import YandexWeatherParser

if __name__ == "__main__":
    yPar = YandexWeatherParser()

    yPar.setPosition(37.6177, 55.755863)
    weather = yPar.get_hourly_weather()

    for i in weather:
        print(i)