from Logger import connect_to_mysql

config = {
    "host": "mysql.joinserver.xyz",
    "port": "3306",
    "user": "u364023_5LPVtbSpGQ",
    "password": "yReHGgJ@QRtGvg5MdCL3h.eF",
    "database": "s364023_ITMyGIS",
}

def sql_connector():
    cnx = connect_to_mysql(config, attempts=3)
    return cnx, cnx.cursor()