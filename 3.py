from geopy import distance
import mysql.connector

icao_koodi_1 = input("Anna ICAO koodi 1: ")
connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='',
    autocommit=True
)

icao_koodi_2 = input("Anna ICAO koodi 2: ")

koodi_1 = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident=%s"
koodi_2 = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident=%s"

cursor = connection.cursor()

cursor.execute(koodi_1, (icao_koodi_1,))
result_1 = cursor.fetchall()

cursor.execute(koodi_2, (icao_koodi_2,))
result_2 = cursor.fetchall()

välimatka = distance.distance(result_1, result_2).km


print(f"Välimatka on: {välimatka:.2f} km")