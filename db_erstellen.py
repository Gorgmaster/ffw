import sqlite3

try:
    # Verbindung zur SQLite-Datenbank herstellen (Datei wird erstellt, falls sie nicht existiert)
    conn = sqlite3.connect('zeitsteuerung.db')
    cursor = conn.cursor()

    # Tabelle erstellen (sicherstellen, dass die Tabelle nicht schon existiert)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS zeitsteuerung (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        an TEXT NOT NULL,
        aus TEXT NOT NULL
    );
    ''')

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    print("Datenbank und Tabelle wurden erfolgreich erstellt.")

except sqlite3.Error as e:
    print(f"Fehler: {e}")
finally:
    conn.close()