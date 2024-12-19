import sqlite3

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('zeitsteuerung.db')
cursor = conn.cursor()

# Abfrage, um alle Daten aus der Tabelle zu holen
cursor.execute("SELECT * FROM zeitsteuerung")

# Alle Zeilen der Tabelle abrufen
rows = cursor.fetchall()

# Ausgeben der Daten
if rows:
    print("Daten aus der Tabelle 'zeitsteuerung':")
    for row in rows:
        print(f"ID: {row[0]}, An: {row[1]}, Aus: {row[2]}")
else:
    print("Keine Daten in der Tabelle vorhanden.")

# Verbindung schließen
conn.close()
