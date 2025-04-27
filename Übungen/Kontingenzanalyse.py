import pandas as pd
import numpy as np
import Berechnungssfunktionen as bf

# Daten der Kontingenztabelle
data = {
    "Nebenjob X": ["x1 = ja", "x2 = nein", "insgesamt"],
    "y1 = unbefriedigend": [10, 65, 75],
    "y2 = befriedigend": [190, 17, 207],
    "insgesamt": [200, 82, 282]
}

# DataFrame erstellen
df = pd.DataFrame(data)

# DataFrame anzeigen
print(df)

a = [df["y1 = unbefriedigend"][0], df["y2 = befriedigend"][0]]
b = [df["y1 = unbefriedigend"][1], df["y2 = befriedigend"][1]]

chi_quadrat = bf.chi_quadrat_wert(a, b)
print(chi_quadrat)

phi_koeffizient = bf.phi_koeffizient_wert(chi_quadrat, df["y1 = unbefriedigend"].iloc[:2])
print(phi_koeffizient)

