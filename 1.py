import mysql.connector

connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='lp',
         user='root',
         password='',
         autocommit=True
         )

icao_koodi = input("Anna ICAO koodi: ")

koodi_tietokannassa = "SELECT name, municipality FROM airport WHERE ident=%s"
cursor = connection.cursor()
cursor.execute(koodi_tietokannassa, (icao_koodi,))

results = cursor.fetchone()

if results:
    print(f"Lentoasema on {results[0]}, paikka on {results[1]}")


else:
    print("Koodi on väärin")

cursor.close()
connection.close()