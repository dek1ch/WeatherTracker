from YandexWeatherParser import WeatherParser

if __name__ == "__main__":
    par = WeatherParser()

    par.setPosition(37.6177, 55.755863)
    weather = par.get_hourly_weather()

    for i in weather:
        print(i)