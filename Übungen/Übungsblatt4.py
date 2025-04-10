import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Daten 
data = {
    "G":  [1,1,1,1,1,1,2,2,1,2,1,1,2,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,2,2],
    "S":  [12,13,12,12,9,12,14,10,18,10,13,15,13,16,14,13,13,17,12,15,13,13,15,13,15,12,14,10,12,17,11,14,11,13,11,7],
    "E":  [1,3,5,2,3,2,5,1,3,3,4,4,2,3,3,2,2,1,2,2,3,4,1,3,4,2,1,2,3,2,1,3,2,2,3,1],
    "D":  [3,4,4,3,4,1,3,4,3,4,4,3,2,3,4,3,4,4,2,3,4,3,4,2,4,4,3,4,3,3,4,2,1,4,4,4],
    "N":  [2,2,3,3,2,1,5,2,1,3,3,2,2,2,2,2,2,3,2,3,2,3,2,2,3,2,2,2,2,2,2,3,2,3,3,2],
}

df = pd.DataFrame(data)

# Aufgabe 1
# Berechnen Sie für das Merkmal Studiendauer aus der Aufgabe 1 des Aufgabenblatts 2 die folgenden Lage‐ und Streuparameter:
# • Modus/Modalwert
# • unteres, mittleres und oberes Quartil
# • arithmetisches Mittel
# • Spannweite
# • Interquartilsabstand

modalwert = df["S"].mode()[0]
unteres_quartil = df["S"].quantile(0.25)
mittleres_quartil = df["S"].quantile(0.5)
oberes_quartil = df["S"].quantile(0.75)
arithmetisches_mittel = df["S"].mean()
spannweite = df["S"].max() - df["S"].min()
interquartilsabstand = oberes_quartil - unteres_quartil

print(f"Modalwert: {modalwert}")
print(f"Unteres Quartil: {unteres_quartil}")
print(f"Mittleres Quartil: {mittleres_quartil}")
print(f"Oberes Quartil: {oberes_quartil}")
print(f"Arithmetisches Mittel: {arithmetisches_mittel}")
print(f"Spannweite: {spannweite}")
print(f"Interquartilsabstand: {interquartilsabstand}\n")

# Aufgabe 2
# Berechnen Sie für die Aufgaben 1 und 3 des Aufgabenblatts 3 die folgenden Streuparameter:
# • Modus/Modalwert
# • unteres, mittleres und oberes Quartil
# • arithmetisches Mittel
# • Spannweite
# • Interquartilsabstand

# Aufgabe 1 des Aufgabenblatts 3 
data2 = {
    "Klasse": ["0-<2", "2-<4", "4-<6", "6-<8", "8-<10", "10-<15", "15-<30"],
    "Häufigkeit": [1650, 1111, 720, 508, 332, 427, 252],
    "Klassenbreite": [2, 2, 2, 2, 2, 5, 15],  
    "Klassenmitte": [1, 3, 5, 7, 9, 12.5, 22.5],  
}

df2 = pd.DataFrame(data2)

df2["Relative Häufigkeit"] = df2["Häufigkeit"] / df2["Häufigkeit"].sum()
df2["Klassendichte"] = df2["Relative Häufigkeit"] / df2["Klassenbreite"]
df2["Kumulierte Häufigkeit"] = df2["Relative Häufigkeit"].cumsum()

modalwert2 = df2.loc[df2["Häufigkeit"].idxmax(), "Klassenmitte"]

unteres_quartil2 = 0.25 / df2[df2["Klasse"] == "0-<2"]["Klassendichte"].values[0]

mittleres_quartil2 = df2[df2["Kumulierte Häufigkeit"] >= 0.5].iloc[0]["Klasse"].split("-")[0]
mittleres_quartil2 = float(mittleres_quartil2) + (0.5 - df2[df2["Kumulierte Häufigkeit"] < 0.5]["Kumulierte Häufigkeit"].values[-1]) / df2[df2["Klasse"] == "2-<4"]["Klassendichte"].values[0]

oberes_quartil2 = df2[df2["Kumulierte Häufigkeit"] >= 0.75].iloc[0]["Klasse"].split("-")[0]
oberes_quartil2 = float(oberes_quartil2) + (0.75 - df2[df2["Kumulierte Häufigkeit"] < 0.75]["Kumulierte Häufigkeit"].values[-1]) / df2[df2["Klasse"] == "6-<8"]["Klassendichte"].values[0]

arithmetisches_mittel2 = (df2["Klassenmitte"] * df2["Relative Häufigkeit"]).sum()
spannweite2 = 30 - 0
interquartilsabstand2 = oberes_quartil2 - unteres_quartil2

print(f"\nModalwert: {modalwert2}")
print(f"Unteres Quartil: {unteres_quartil2}")
print(f"Mittleres Quartil: {mittleres_quartil2}")
print(f"Oberes Quartil: {oberes_quartil2}")
print(f"Arithmetisches Mittel: {arithmetisches_mittel2}")
print(f"Spannweite: {spannweite2}")
print(f"Interquartilsabstand: {interquartilsabstand2}\n")

# Aufgabe 3 des Aufgabenblatts 3
da = {
    "Klasse Kj": ["100 -< 300", "300 -< 600", "600 -< 900", "900 -< 1200", "1200 -< 1500", "1500 -< 2000"],
    "n NRW": [5, 27, 35, 21, 8, 4],
    "n BY": [5, 32, 47, 12, 3, 1],
    "Klassenbreite": [200, 300, 300, 300, 300, 500],
    "Klassenmitten": [200, 450, 750, 1050, 1350, 1750],
    "h NRW": [0.05, 0.27, 0.35, 0.21, 0.08, 0.04],
    "h BY": [0.05, 0.32, 0.47, 0.12, 0.03, 0.01],
    "F(X) NRW": [0.05, 0.32, 0.67, 0.88, 0.96, 1.00],
    "F(X) BY": [0.05, 0.37, 0.84, 0.96, 0.99, 1.00],
    "f(n NRW)": [0.00025, 0.0009, 0.00116667, 0.0007, 0.00026667, 0.00008],
    "f(n BY)": [0.00025, 0.00106667, 0.00156667, 0.0004, 0.0001, 0.00002],
}
df3 = pd.DataFrame(da)

modalwertNRW = df3.loc[df3["n NRW"].idxmax(), "Klassenmitten"]

unteres_quartilNRW = df3[df3["F(X) NRW"] >= 0.25].iloc[0]["Klasse Kj"].split(" -< ")[0]
unteres_quartilNRW = float(unteres_quartilNRW) + (0.25 - df3[df3["F(X) NRW"] < 0.25]["F(X) NRW"].values[-1]) / df3[df3["Klasse Kj"] == "300 -< 600"]["f(n NRW)"].values[0]

mittleres_quartilNRW = df3[df3["F(X) NRW"] >= 0.5].iloc[0]["Klasse Kj"].split(" -< ")[0]
mittleres_quartilNRW = float(mittleres_quartilNRW) + (0.5 - df3[df3["F(X) NRW"] < 0.5]["F(X) NRW"].values[-1]) / df3[df3["Klasse Kj"] == "600 -< 900"]["f(n NRW)"].values[0]

oberes_quartilNRW = df3[df3["F(X) NRW"] >= 0.75].iloc[0]["Klasse Kj"].split(" -< ")[0]
oberes_quartilNRW = float(oberes_quartilNRW) + (0.75 - df3[df3["F(X) NRW"] < 0.75]["F(X) NRW"].values[-1]) / df3[df3["Klasse Kj"] == "900 -< 1200"]["f(n NRW)"].values[0]

arithmetisches_mittelNRW = (df3["Klassenmitten"] * df3["h NRW"]).sum()
spannweiteNRW = 2000 - 100
interquartilsabstandNRW = oberes_quartilNRW - unteres_quartilNRW

print(f"\nModalwert NRW: {modalwertNRW}")
print(f"Unteres Quartil NRW: {unteres_quartilNRW}")
print(f"Mittleres Quartil NRW: {mittleres_quartilNRW}")
print(f"Oberes Quartil NRW: {oberes_quartilNRW}")
print(f"Arithmetisches Mittel NRW: {arithmetisches_mittelNRW}")
print(f"Spannweite NRW: {spannweiteNRW}")
print(f"Interquartilsabstand NRW: {interquartilsabstandNRW}\n")

modalwertBY = df3.loc[df3["n BY"].idxmax(), "Klassenmitten"]

unteres_quartilBY = df3[df3["F(X) BY"] >= 0.25].iloc[0]["Klasse Kj"].split(" -< ")[0]
unteres_quartilBY = float(unteres_quartilBY) + (0.25 - df3[df3["F(X) BY"] < 0.25]["F(X) BY"].values[-1]) / df3[df3["Klasse Kj"] == "300 -< 600"]["f(n BY)"].values[0]

mittleres_quartilBY = df3[df3["F(X) BY"] >= 0.5].iloc[0]["Klasse Kj"].split(" -< ")[0]
mittleres_quartilBY = float(mittleres_quartilBY) + (0.5 - df3[df3["F(X) BY"] < 0.5]["F(X) BY"].values[-1]) / df3[df3["Klasse Kj"] == "600 -< 900"]["f(n BY)"].values[0]

oberes_quartilBY = df3[df3["F(X) BY"] >= 0.75].iloc[0]["Klasse Kj"].split(" -< ")[0]
oberes_quartilBY = float(oberes_quartilBY) + (0.75 - df3[df3["F(X) BY"] < 0.75]["F(X) BY"].values[-1]) / df3[df3["Klasse Kj"] == "600 -< 900"]["f(n BY)"].values[0]

arithmetisches_mittelBY = (df3["Klassenmitten"] * df3["h BY"]).sum()
spannweiteBY = 2000 - 100
interquartilsabstandBY = oberes_quartilBY - unteres_quartilBY

print(f"Modalwert BY: {modalwertBY}")
print(f"Unteres Quartil BY: {unteres_quartilBY}")
print(f"Mittleres Quartil BY: {mittleres_quartilBY}")
print(f"Oberes Quartil BY: {oberes_quartilBY}")
print(f"Arithmetisches Mittel BY: {arithmetisches_mittelBY}")
print(f"Spannweite BY: {spannweiteBY}")
print(f"Interquartilsabstand BY: {interquartilsabstandBY}")

# Aufgabe 3

# Daten
werte = [8, 0, 17, 12, 22, 3, 5, 52, 1, 42, 8, 12, 10, 19, 21, 6, 5, 33, 36, 6]
klassen = ["0-<10", "10-<20", "20-<30", "30-<40", "40-<52"]

# Klassenbreite berechnen
bins = [0, 10, 20, 30, 40, 52]  # Klassenränder
df4 = pd.cut(werte, bins=bins, right=False).value_counts().sort_index()

# DataFrame erstellen
data3 = {
    "Klasse": klassen,
    "Häufigkeit": df4.values,
    "Klassenbreite": [10, 10, 10, 10, 12],
    "Klassenmitte": [5, 15, 25, 35, 46],
}

df_klassen = pd.DataFrame(data3)

df_klassen["Relative Häufigkeit"] = df_klassen["Häufigkeit"] / df_klassen["Häufigkeit"].sum()
df_klassen["Klassendichte"] = df_klassen["Relative Häufigkeit"] / df_klassen["Klassenbreite"]
df_klassen["Kumulative Häufigkeit"] = df_klassen["Relative Häufigkeit"].cumsum()

print(df_klassen)

F_25 = df_klassen[df_klassen["Klasse"] == "10-<20"]["Kumulative Häufigkeit"].values[0] + df_klassen[df_klassen["Klasse"] == "20-<30"]["Klassendichte"].values[0] * (25-20)
print(f"\nF(25) = {F_25:.3f}")

oberes_quartil3 = df_klassen[df_klassen["Kumulative Häufigkeit"] >= 0.75].iloc[0]["Klasse"].split("-<")[0]
oberes_quartil3 = float(oberes_quartil3) + (0.75 - df_klassen[df_klassen["Kumulative Häufigkeit"] < 0.75]["Kumulative Häufigkeit"].values[-1]) / df_klassen[df_klassen["Klasse"] == "20-<30"]["Klassendichte"].values[0]
print(oberes_quartil3)
