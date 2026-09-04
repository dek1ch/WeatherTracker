import requests
from bs4 import BeautifulSoup

latitude = 55.79
longitude = 37.595556

url = f"https://yandex.ru/pogoda/ru/moscow?lat={latitude}&lon={longitude}"

response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

page_text = soup.get_text()

if __name__ == "__main__":
    with open("test.html", "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    info = soup.find_all('li', class_='AppHourlyItem_container__aqC1z')

    if info:
        with open("test.txt", "w", encoding="utf-8") as f:
            for i in info:
                weather = i.find('p', class_="A11Y_visuallyHidden__y0sw0 visuallyHidden").text.strip()
                f.write(weather + f"\n")
            print(len(info))