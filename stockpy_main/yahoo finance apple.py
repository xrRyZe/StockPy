import pandas as pd
import yfinance as yf

# Symbol für das gewünschte Unternehmen (z. B. AAPL für Apple)
ticker_symbol = 'AAPL'

# Startdatum und Enddatum für die historischen Daten
start_date = '2023-01-01'
end_date = '2024-01-01'

# Abrufen der historischen Daten von Yahoo Finance
data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Speichern der Daten in eine CSV-Datei
data.to_csv('AAPL.csv')