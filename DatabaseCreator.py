from Connector import sql_connector
import mysql.connector
cnx, cursor = sql_connector()
TABLES = {}

#city {1: Новосибирск, 2: Москва, 3: Питер}
TABLES['users'] = (
    "CREATE TABLE `users`("
    "  `id` int NOT NULL AUTO_INCREMENT UNIQUE,"
    "  `tg_id` int NOT NULL UNIQUE," #Айди телеграмм профиля
    "  `city` TINYINT NOT NULL," #Город выбранный пользователем
    "  `w_food` TINYINT NOT NULL," #Ограничения по еде
    "  `w_fear` TINYINT NOT NULL," #Ограничения по фобиям
    "  `w_health` TINYINT NOT NULL," #Ограничения по здоровью
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['history'] = (
    "CREATE TABLE `history`("
    "  `id` int NOT NULL AUTO_INCREMENT UNIQUE,"
    "  `u_id` int NOT NULL," #Вторичный ключ, ключ пользователя
    "  `city` TINYINT NOT NULL," #Город места
    "  `date` date NOT NULL," #Дата создания истории
    "  `title` varchar(50) NOT NULL," #Название места
    "  `link` MEDIUMTEXT NOT NULL," #Ссылка на 2GIS страничку
    "  `type` TINYINT NOT NULL," #Тип заведения
    "  PRIMARY KEY (`id`),"
    "  CONSTRAINT `history_ibfk_2` FOREIGN KEY (`u_id`) "
    "     REFERENCES `users` (`id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()