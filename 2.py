import mysql.connector

connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='',
         autocommit=True
         )

maa_koodi = input("Anna maa koodi: ")

koodi_tietokannassa = "SELECT name, type FROM airport WHERE iso_country=%s ORDER BY name ASC"
cursor = connection.cursor()
cursor.execute(koodi_tietokannassa, (maa_koodi,))

results = cursor.fetchall()
if results:
    for item in results:
        print(item)
else:
    print("Koodi on väärin")

cursor.close()
connection.close()
