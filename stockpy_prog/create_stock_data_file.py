import pandas as pd
import yfinance as yf
import datetime as dt

start_date = '2023-01-01'
# end_date = '2024-01-01'

def create_stock_data_file(stock_short_code:str):
    # Abrufen der historischen Daten von Yahoo Finance
    data = yf.download(stock_short_code, start=start_date, end=dt.datetime.now().strftime('%Y-%m-%d'))

    # Speichern der Daten in eine CSV-Datei
    data.to_csv(f'./stock_data/{stock_short_code}.csv')
    print(f"Daten von {stock_short_code} erfolgreich gespeichert.")

# create_stock_data_file('AAPL')



# # Symbol für das gewünschte Unternehmen (z. B. AAPL für Apple)
# ticker_symbol = 'AAPL'

# # Startdatum und Enddatum für die historischen Daten

# # Abrufen der historischen Daten von Yahoo Finance
# data = yf.download(ticker_symbol, start=start_date, end=end_date)

# # Speichern der Daten in eine CSV-Datei
# data.to_csv('./stock_data/AAPL.csv')
# print(f"Daten von {ticker_symbol} erfolgreich gespeichert.")
