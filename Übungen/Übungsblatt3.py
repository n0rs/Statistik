import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    "Klasse": ["0-<2", "2-<4", "4-<6", "6-<8", "8-<10", "10-<15", "15-<30"],
    "Häufigkeit": [1650, 1111, 720, 508, 332, 427, 252]
}
df = pd.DataFrame(data)

# Aufgabe 1
# Wie lauten die relativen Häufigkeiten der einzelnen Klassen?
df["Relative Häufigkeit"] = df["Häufigkeit"] / df["Häufigkeit"].sum()

# Aufgabe 2
# Wie breit sind die jeweiligen Klassen?
df["Klassenbreite"] = [2, 2, 2, 2, 2, 5, 15]

# Aufgabe 3
# Wie lauten die Klassenmitten?
df["Klassenmitte"] = [1, 3, 5, 7, 9, 12.5, 22.5]

# Aufgabe 4
# Berechnen Sie die jeweiligen Klassendichten
df["Klassendichte"] = df["Relative Häufigkeit"] / df["Klassenbreite"]

# Aufgabe 5
# Erstellen Sie auf dieser Grundlage ein Histogramm
bins = [0, 2, 4, 6, 8, 10, 15, 30]  # Klassenränder

plt.figure(figsize=(10, 6))
plt.bar(bins[:-1], df["Klassendichte"], width=[2, 2, 2, 2, 2, 5, 15], align="edge", color="blue", alpha=0.5)
plt.xlabel("Klasse")
plt.ylabel("Relative Häufigkeit")
plt.title("Histogramm der relativen Häufigkeiten")
plt.tight_layout()
# plt.show()

# Aufgabe 6
# Berechnen Sie F(7)
df["Kumulierte Häufigkeit"] = df["Relative Häufigkeit"].cumsum()
print(df)
F_7 = df[df["Klasse"] == "4-<6"]["Kumulierte Häufigkeit"].values[0] + df[df["Klasse"] == "6-<8"]["Klassendichte"].values[0] * (7-6)
print(f"F(7) = {F_7:.3f}")

# Aufgabe 7
# Bestimmten Sie x_0,75, d.h. das 0,75-Quantil
x_0_75 = df[df["Kumulierte Häufigkeit"] >= 0.75].iloc[0]["Klasse"].split("-")[0]
x_0_75 = float(x_0_75) + (0.75 - df[df["Kumulierte Häufigkeit"] < 0.75]["Kumulierte Häufigkeit"].values[-1]) / df[df["Klasse"] == "6-<8"]["Klassendichte"].values[0]
print(f"x_0,75 = {x_0_75:.2f}")

# Aufgabe 8
data = {
    "Einkommensklasse": ["1500-<2000", "2000-<2500", "2500-<3000", "3000-<4000", "4000-<5000", "5000-<6500"],
    "Absolute Häufigkeit": [5, 6, 8, 3, 1, 2],
    "Klassenbreite": [500, 500, 500, 1000, 1000, 1500],  
    "Klassenmitte": [1750, 2250, 2750, 3500, 4500, 5750],  
}

df2 = pd.DataFrame(data)
df2["Relative Häufigkeit"] = df2["Absolute Häufigkeit"] / sum(df2["Absolute Häufigkeit"])  # h(i)
df2["Dichtefunktion"] = df2["Relative Häufigkeit"] / df2["Klassenbreite"]  # f(i)
df2["Kumulative Häufigkeit"] = df2["Relative Häufigkeit"].cumsum()  # F(x)
print(df2)

y_0_25 = df2[df2["Kumulative Häufigkeit"] >= 0.25].iloc[0]["Einkommensklasse"].split("-<")[0]
print(y_0_25)
y_0_25 = float(y_0_25) + (0.25 - df2[df2["Kumulative Häufigkeit"] < 0.25]["Kumulative Häufigkeit"].values[-1]) / df2[df2["Einkommensklasse"] == "2000-<2500"]["Dichtefunktion"].values[0]
print(f"y_0,25 = {y_0_25}\n")

y_0_5 = df2[df2["Kumulative Häufigkeit"] >= 0.5].iloc[0]["Einkommensklasse"].split("-<")[0]
print(y_0_5)
y_0_5 = float(y_0_5) + (0.5 - df2[df2["Kumulative Häufigkeit"] < 0.5]["Kumulative Häufigkeit"].values[-1]) / df2[df2["Einkommensklasse"] == "2500-<3000"]["Dichtefunktion"].values[0]
print(f"y_0,5 = {y_0_5}\n")

y_0_75 = df2[df2["Kumulative Häufigkeit"] >= 0.75].iloc[0]["Einkommensklasse"].split("-<")[0]
print(y_0_75)
y_0_75 = float(y_0_75) + (0.75 - df2[df2["Kumulative Häufigkeit"] < 0.75]["Kumulative Häufigkeit"].values[-1]) / df2[df2["Einkommensklasse"] == "2500-<3000"]["Dichtefunktion"].values[0]
print(f"y_0,75 = {y_0_75}")

# Aufgabe 9
# den Merkmalsträger, die jeweilige statistische Gesamtheit, das jeweilige Erhebungsmerkmal und seine Skalierung benennen.

# Merkmalsträger: Die befragten Energieausgleichszahlungsempfänger der Länder NRW & Bayern
# stat. Gesamtheit: Alle Energieausgleichszahlungsempfänger der Länder NRW & BY
# Erhebungsmerkmal: Die Höher der Zahlungen
# Skalierung: quantitativ-stetig, wenn bei der Erhebung tatsächliche Zahlen erhoben wurden // qualititiv ordinal, sollten bei Erhebung bereits Klassen vorgegeben sein

# Aufgabe 10
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
print(df3)

F_500_NRW = df3[df3["Klasse Kj"] == "100 -< 300"]["F(X) NRW"].values[0] + df3[df3["Klasse Kj"] == "300 -< 600"]["f(n NRW)"].values[0] * (500-300)
print(f"F(500 NRW) = {F_500_NRW:.3f}")

F_500_BY = df3[df3["Klasse Kj"] == "100 -< 300"]["F(X) BY"].values[0] + df3[df3["Klasse Kj"] == "300 -< 600"]["f(n BY)"].values[0] * (500-300)
print(f"F(500 BY) = {F_500_BY:.3f}")

F_09_NRW = df3[df3["F(X) NRW"] >= 0.9].iloc[0]["Klasse Kj"].split(" -< ")[0]
F_09_NRW = float(F_09_NRW) + (0.9 - df3[df3["F(X) NRW"] < 0.9]["F(X) NRW"].values[-1]) / df3[df3["Klasse Kj"] == "1200 -< 1500"]["f(n NRW)"].values[0]
print(f"x_0,9_NRW = {F_09_NRW:.2f}")

F_09_BY = df3[df3["F(X) BY"] >= 0.9].iloc[0]["Klasse Kj"].split(" -< ")[0]
F_09_BY = float(F_09_BY) + (0.9 - df3[df3["F(X) BY"] < 0.9]["F(X) BY"].values[-1]) / df3[df3["Klasse Kj"] == "900 -< 1200"]["f(n BY)"].values[0]
print(f"x_0,9_BY = {F_09_BY:.2f}")



# Korrigierte Klassenränder (nur untere Grenzen der Klassen)
bins = [100, 300, 600, 900, 1200, 1500, 2000]  # 6 Werte, passend zu den Klassen

fig, axes = plt.subplots(1, 2, figsize=(10, 6))

# Balkendiagramm für NRW
axes[0].bar(bins[:-1], df3["f(n NRW)"], width=df3["Klassenbreite"], align="edge", color="blue", alpha=0.5)
axes[0].set_title("Histogramm der relativen Häufigkeiten (NRW)")
axes[0].set_xlabel("Klasse")
axes[0].set_ylabel("Dichtefunktion")

# Balkendiagramm für Bayern
axes[1].bar(bins[:-1], df3["f(n BY)"], width=df3["Klassenbreite"], align="edge", color="green", alpha=0.5)
axes[1].set_title("Histogramm der relativen Häufigkeiten (Bayern)")
axes[1].set_xlabel("Klasse")
axes[1].set_ylabel("Dichtefunktion")

plt.tight_layout()
# plt.show()


