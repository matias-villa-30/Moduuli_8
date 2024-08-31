import mysql.connector

connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='',
         autocommit=True
         )

icao_koodi = input("Anna ICAO koodi: ")

koodi_tietokannassa = "SELECT name FROM airport WHERE ident=%s"
cursor = connection.cursor()
cursor.execute(koodi_tietokannassa, (icao_koodi,))

results = cursor.fetchone()

if results:
    for item in results:
        print(f"Lentoasema on: {item}")


else:
    print("Koodi on väärin")

cursor.close()
connection.close()
