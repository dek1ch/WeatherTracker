from WeatherParser import YandexWeatherParser
from geopy.geocoders import Nominatim

if __name__ == "__main__":
    yPar = YandexWeatherParser()
    geolocator = Nominatim(user_agent="weather parser")

    point = input("Введите место отслеживания погоды: ")

    location = geolocator.geocode(point)

    if location:
        print(f"Широта: {location.latitude}")
        print(f"Долгота: {location.longitude}")
        print(f"Полная информация: {location.raw}")

        yPar.setPosition(location.longitude, location.latitude)
        weather = yPar.get_hourly_weather()

        for i in weather:
            print(i)
    else:
        print(f"Место {point} не найдено.")