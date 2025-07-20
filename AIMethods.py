from dotenv import load_dotenv
load_dotenv('.env')
from os import getenv
from openai import OpenAI
import pandas as pd

def akinator(prompt: str, city: int, message: list):

  client = OpenAI(api_key=getenv('OPENAI_API_KEY'))
  completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=message
  )

  cities = {1: "Новосибирск", 2:"Москва", 3:"Санкт-Петербург"}
  city = cities[1]
  df = pd.read_csv("placesNSK.csv")
  message=[
      {'role': "developer",
       'content': df,
       "role": "developer",
       "content": f"Ты ITMyGIS нейронная сеть - Акинатор. Ты являешься самым большим знатоком о всех постройках или просто местах для отдыха в городе {city}, помоги пользователю найти идеальное место для отдыха из списка (df), у тебя есть максимум 10 вопросов, вопрос это место подходит тоже считается, так-же ты обязан предложить пользователю 3 варианта ответа, пронумеровав их так. 1 текст первого варианта ответа\n 2 текст второго варианта ответа\n 3 текст третьего варианта ответа\n"},
    ]
  a = completion.choices[0].message.content
  l = message
  z = prompt
  l.append({'role': 'system', 'content': a})
  l.append({'role': 'user', 'content': prompt})
  message = l.copy()
  return a, l

