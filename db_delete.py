import sqlite3
from datetime import datetime

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('zeitsteuerung.db')
cursor = conn.cursor()

# SQL-Befehl ausführen
cursor.execute("DELETE FROM zeitsteuerung WHERE aus < DATETIME('2024-12-18 23:15:00')")

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()