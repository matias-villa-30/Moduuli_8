import mysql.connector

connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='airports',
         user='root',
         password='',
         autocommit=True
         )

icao_koodi = input("Anna ICAO koodi: ")

koodi_tietokannassa = "SELECT * FROM airports WHERE name=%s"
cursor = connection.cursor()
cursor.execute(koodi_tietokannassa, (icao_koodi,))

results = cursor.fetchall()

if results:
    first_result = results[0]
    kaupunki = first_result[3]
    paikka = first_result[0]
    print(f"Lentoaseman kaupunki on: {kaupunki}")
    print(f"Lentoaseman tietokannan paikka on: {paikka}")

else:
    print("Koodi on väärin")

cursor.close()
connection.close()
