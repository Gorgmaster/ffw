import sqlite3

conn = sqlite3.connect('zeitsteuerung.db')
cursor = conn.cursor()

# Überprüfen, ob die Tabelle existiert
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='zeitsteuerung';")
result = cursor.fetchone()

if result:
    print("Tabelle existiert.")
    cursor.executemany('''
    INSERT INTO zeitsteuerung (an, aus) VALUES (?, ?);
    ''', [
        ('2024-12-18 10:00:00', '2024-12-18 15:00:00'),
        ('2024-12-18 20:00:00', '2024-12-18 23:00:00')
    ])
    conn.commit()
else:
    print("Tabelle existiert nicht.")

conn.close()
