import psycopg2

if __name__ == "__main__":
    try:
        url = "host='{0}' dbname='{1}' user='{2}' password='{3}'".format('localhost', 'shopdb', 'postgres', 'Yareli@0907')


        conn = psycopg2.connect(url)


        cursor = conn.cursor()

        with open("client.sql", "r") as sql_file:
            sql_commands = sql_file.read()

            cursor.execute(sql_commands)

        conn.commit()
        cursor.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
