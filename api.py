import os
import requests
from dotenv import load_dotenv

# Dict of cities - {city : lat, lng}
from data import CITIES

load_dotenv()

# get API info from .env
API_KEY = os.getenv('API_KEY')
API_URL_LIST = os.getenv('API_URL_LIST')


def get_fuel_price(city, fuel_type="all", radius=5, sort="dist"):
    if city in CITIES:
        lat, lng = CITIES[city]
        url = f'{API_URL_LIST}?lat={lat}&lng={lng}&rad={radius}&type={fuel_type}&sort={sort}&apikey={API_KEY}'

        try:
            response = requests.get(url)

            data = response.json()
            if not data.get('ok', False):
                return {'error': f"API помилка: {data.get('message', 'Невідома помилка')}"}

            if response.status_code == 200:
                return data
            else:
                return {'error': f'Не вдалося отримати дані. Код помилки: {response.status_code}'}

        except requests.exceptions.RequestException as e:
            return {'error': f'Помилка при з\'єднанні з сервером: {e}'}
    else:
        return {'error': 'Місто ще не додано до списку'}


def response_fuel_price(selected_city, label):
    data = get_fuel_price(selected_city)
    if 'error' in data:
        label.text = data['error']
    else:
        stations = data.get('stations', [])

        if stations:
            result = f"Ціни на пальне у місті {selected_city}:\n"

            for station in stations:
                name = station.get('name', 'Невідомо')
                street = station.get('street', 'Невідомо')
                place = station.get('place', 'Невідомо')
                distance = station.get('dist', 'Невідомо')
                diesel_price = station.get('diesel', 'Невідомо')
                e5_price = station.get('e5', 'Невідомо')
                e10_price = station.get('e10', 'Невідомо')

                result += f"\nЗаправка: {name}\nАдреса: {street}, {place}\nВідстань: {distance} км\nЦіни:\n" \
                          f"Diesel: {diesel_price} EUR\nE5: {e5_price} EUR\nE10: {e10_price} EUR\n{'-' * 40}\n"

            label.text = result
        else:
            label.text = "Ціни не знайдені або заправки не виявлені."
