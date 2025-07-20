from dotenv import load_dotenv
load_dotenv('.env')
from os import getenv
#from openai import AsyncClient
from openai import OpenAI

def akinator(prompt: str, city: int, message: list):
  client = OpenAI(api_key=getenv('OPENAI_API_KEY'))
  completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=message
  )

  return completion.choices[0].message.content, message
cities = {1: "Новосибирск", 2:"Москва", 3:"Санкт-Петербург"}
z = ""
city = cities[1]
message=[
      {'role': "developer",
       'content': "Закинуть данные из placesNSK",
       "role": "developer",
       "content": f"Для начала, представься перед пользователем, ты ITMyGIS нейронная сеть - Акинатор. Ты являешься самым большим знатоком о всех постройках или просто местах для отдыха в городе {city}, помоги пользователю найти идеальное место для отдыха, у тебя есть максимум 10 вопросов, вопрос это место подходит тоже считается, так-же ты обязан предложить пользователю 3 варианта ответа, пронумеровав их так. 1 текст первого варианта ответа\n 2 текст второго варианта ответа\n 3 текст третьего варианта ответа\n"},
    ]
while True:
  a, l = akinator(prompt=z, city=1, message=message)
  print(a)
  l.append({'role': 'system', 'content': a})
  z = input()
  l.append({'role': 'user', 'content': z})
  message = l.copy()