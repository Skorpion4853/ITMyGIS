import requests
import pandas
import json
from dotenv import load_dotenv
load_dotenv('.env')
from os import getenv


cities = {"Москва": 4504222397630173, 'Санкт-Петербург': 5348647327760881, 'Новосибирск': 141360258613345}
types = ['поесть', 'достопримечательности', 'развлечения', 'места для отдыха', 'супермаркеты']
ids = ['12127', '1203', '70348', '162', '518', '110304', '110430', '16743', '159', '112907', '165', '270', '112668', '112720', '112670', '350', '112550', '170', '112900', '112906', '110345', '161', '111526', '547', '11647', '9777', '112647', '111593', '112658', '24099']

for type in types:
    url = f"https://catalog.api.2gis.com/3.0/items?q={type}&fields=items.reviews&city_id=141360258613345&key={getenv('GIS_KEY')}"
    response = requests.get(url)
    for res in response.json()['result']['items']:
        print(res)