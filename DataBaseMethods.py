import pandas as pd
from Connector import sql_connector
from datetime import datetime

#получаем курсор и коннектор


#Добавление пользователя | регистрация
def add_user(tg_id: int, city: int) -> None:
    cnx, cursor = sql_connector()
    user = [tg_id, city, 0, 0, 0]
    query = ('INSERT INTO users'
             '(tg_id, city, w_food, w_fear, w_health)'
             'VALUES (%s, %s, %s, %s, %s)')
    cursor.execute(query, user)
    cnx.commit()
    cursor.close()
    cnx.close()

#Добавление записи истории использования бота
def add_history(tg_id: int, title: str, link: str, type=0) -> None:
    cnx, cursor = sql_connector()
    cursor.execute(f"""SELECT city FROM users
        WHERE tg_id = {tg_id}""")
    city = cursor.fetchone()[0]
    user = [tg_id, city, datetime.now(), title, link, type]
    query = ('INSERT INTO history'
             '(u_id, city, date, title, link, type)'
             'VALUES (%s, %s, %s, %s, %s, %s)')
    cursor.execute(query, user)
    cnx.commit()
    cursor.close()
    cnx.close()


#Изменение настроек пользователя
def setting_user(tg_id: int, city: int, w_food: int, w_fear: int, w_health: int) -> None:
    cnx, cursor = sql_connector()
    query = "UPDATE users SET tg_id = %s, city = %s, w_food = %s, w_fear = %s, w_health = %s WHERE tg_id = %s"
    cursor.execute(query, [tg_id, city, w_food, w_fear, w_health, tg_id])
    cnx.commit()
    cursor.close()
    cnx.close()

#Возврат топ 5 по городу
def top_5(tg_id: int) -> list:
    cnx, cursor = sql_connector()
    cursor.execute(f"""SELECT city FROM users
    WHERE tg_id = {tg_id}""")
    city = cursor.fetchone()[0]
    cursor.execute(f"""SELECT * FROM history
    WHERE city = {city}""")
    df = pd.DataFrame(columns=['id', 'tg_id', 'city', 'date', 'title', 'link', 'type'], data=cursor.fetchall())
    lst = df.title.value_counts().to_dict().keys()
    lst = list(lst)[0:6]
    lst1 = df.link.value_counts().to_dict().keys()
    lst1 = list(lst1)[0:6]
    result = []
    for i in range(len(lst)):
        result.append([lst[i], lst1[i]])
    cursor.close()
    cnx.close()
    return result

#Последние 5 заведений пользователя
def history(tg_id: int) -> list:
    cnx, cursor = sql_connector()
    cursor.execute(f"""SELECT * FROM history
        WHERE u_id = {tg_id}""")
    df = pd.DataFrame(columns=['id', 'tg_id', 'city', 'date', 'title', 'link', 'type'], data=cursor.fetchall())
    sort_df = df.sort_values('date', ascending=False)
    cursor.close()
    cnx.close()
    return sort_df[["date", "title", "link"]].values[:5]

