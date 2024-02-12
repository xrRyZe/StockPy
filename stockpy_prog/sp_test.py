# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.neural_network import MLPClassifier

# # Laden von Aktiendaten (Beispiel: AAPL von Yahoo Finance)
# data = pd.read_csv('AAPL.csv')  # Stellen Sie sicher, dass die Datei 'AAPL.csv' vorhanden ist

# # Vorbereiten der Daten für das neuronale Netz
# X = data[['Open', 'High', 'Low', 'Volume']].values
# y = np.where(data['Close'].shift(-1) > data['Close'], 1, -1)

# # Aufteilen der Daten in Trainings- und Testsets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Skalierung der Merkmale
# scaler = MinMaxScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

# # Training des neuronalen Netzes
# model = MLPClassifier(hidden_layer_sizes=(50, 50), max_iter=1000, random_state=42)
# model.fit(X_train_scaled, y_train)

# # Auswertung der Genauigkeit des Modells
# accuracy = model.score(X_test_scaled, y_test)
# print(f"Genauigkeit des neuronalen Netzes: {accuracy}")

# # Verwenden des Modells, um Handelssignale zu generieren
# predicted_signals = model.predict(X_test_scaled)
# print("Vorhergesagte Handelssignale:", predicted_signals)

