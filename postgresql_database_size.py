import psycopg2
from tabulate import tabulate

if __name__ == "__main__":
    try:
        url = "host='{0}' dbname='{1}' user='{2}' password='{3}'".format('localhost', 'postgres', 'postgres', 'Yareli@0907')


        conn = psycopg2.connect(url)


        cursor = conn.cursor()

        sql = """SELECT datname, usename, pg_size_pretty(pg_database_size(pg_database.datname))
        FROM pg_database 
        INNER JOIN pg_user 
        ON pg_user.usesysid = datdba"""

        cursor.execute(sql)

        tabla = []

        for row in cursor:
            tabla.append([row[0], row[1], row[2]])

        print(tabulate(tabla, headers=['Base de Datos', 'Usuario', 'Tamaño']))

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)


