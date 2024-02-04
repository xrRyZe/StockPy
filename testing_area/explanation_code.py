# Zuerst wird die hochgeladene CSV-Datei eingelesen, um deren Inhalt zu analysieren.
import pandas as pd

# Einlesen der CSV-Datei
data = pd.read_csv('/mnt/data/AAPL.csv')

# Anzeigen der ersten paar Zeilen der Datei zur Überprüfung
data.head()