import sqlite3
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta

def addTime(day, an, aus):

    onTime = datetime.combine(day, an)
    offTime = datetime.combine(day, aus)
    
    conn = sqlite3.connect('zeitsteuerung.db')
    cursor = conn.cursor()
    
    cursor.execute(f''' INSERT INTO zeitsteuerung (an, aus) VALUES ("{onTime}", "{offTime}")''')
    
    conn.commit()
    
    conn.close()

def getEntries():
    
    conn = sqlite3.connect('zeitsteuerung.db')
    query = "SELECT * FROM zeitsteuerung"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
    
    



st.title('Monitorzeiten eingeben')


day = st.date_input("Tag auswählen: ")

col1, col2 = st.columns(2)

an = col1.time_input('Uhrzeit für "an" ', '19:00')
#uhrzeit = datetime.strptime(an, '%H:%M')
heute = datetime.today()
uhrzeit_as_datetime = datetime.combine(heute, an)

neue_uhrzeit = uhrzeit_as_datetime + timedelta(hours=3)
neue_uhrzeit_str = neue_uhrzeit.strftime('%H:%M')

aus = col2.time_input('Uhrzeit für "aus" ', neue_uhrzeit_str)

button_click = st.button('Monitorzeit hinzufügen')

if button_click:
    addTime(day, an, aus)
    

st.header("Daten aus der Tabelle 'zeitsteuerung'")
    
# Daten aus der Datenbank abfragen
df = getEntries()

# Überprüfen, ob Daten vorhanden sind
if not df.empty:
    # Zeige die Daten als Tabelle an
    st.dataframe(df)
else:
    st.write("Keine Daten in der Tabelle vorhanden.")