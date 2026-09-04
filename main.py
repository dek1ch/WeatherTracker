import requests
from bs4 import BeautifulSoup

url = "https://yandex.ru/pogoda/ru/moscow?lat=55.79&lon=37.595556"

response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

page_text = soup.get_text()

if __name__ == "__main__":
    temperature = soup.find_all('p', class_='AppHourlyItem_main__HNbqX')

    if temperature:
        with open("test.txt", "w", encoding="utf-8") as f:
            for t in temperature:
                f.write(t.get_text(strip=True) + " | ")
            print(len(temperature))