import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import sys
from fpdf import FPDF
import os

# Umleitung der Ausgabe in eine Textdatei
with open("output_Übungsblatt5.txt", "w") as f:
    sys.stdout = f
    # Hier das gesamte Skript ausführen
    print("Ausgabe von Übungsblatt5:")

    # Aufgabe 1
    # Berechnen Sie für das Beispiele auf S. 27 des Skriptes die Varianz und 
    # die Standardabweichung einmal direkt aus der Urliste und einmal aus der Häufigkeitstabelle.

    # Urliste
    data = {
        "i": range(1, 26),
        "Einkommen": [
            1600, 2900, 3200, 4200, 2700, 2050, 3500, 2050, 2100, 2700,
            2150, 1550, 1920, 2150, 3200, 2500, 1800, 1600, 2700, 5100,
            2600, 6250, 2500, 2500, 2200
        ],
        "HH-Größe": [
            1, 4, 2, 5, 5, 1, 3, 2, 1, 1,
            3, 2, 1, 3, 4, 3, 2, 1, 3, 2,
            3, 4, 2, 3, 2
        ]
    }
    df = pd.DataFrame(data)
    print("Aufgabe 1 Urliste")

    # Varianz
    varianz_urliste = df["Einkommen"].var(ddof=0) 
    print(f"\nVarianz aus Urliste: {varianz_urliste:.2f}")

    # Standardabweichung
    std_urliste = varianz_urliste**0.5
    print(f"Standardabweichung aus Urliste: {std_urliste:.2f}\n")

    # Häufigkeitstabelle
    data2 = {
        "Einkommensklasse": ["1500-<2000", "2000-<2500", "2500-<3000", "3000-<4000", "4000-<5000", "5000-<6500"],
        "Absolute Häufigkeit": [5, 6, 8, 3, 1, 2],
        "Klassenbreite": [500, 500, 500, 1000, 1000, 1500],  
        "Klassenmitte": [1750, 2250, 2750, 3500, 4500, 5750],  
    }

    df2 = pd.DataFrame(data2)
    df2["Relative Häufigkeit"] = df2["Absolute Häufigkeit"] / sum(df2["Absolute Häufigkeit"])  # h(i)
    df2["Dichtefunktion"] = df2["Relative Häufigkeit"] / df2["Klassenbreite"]  # f(i)
    df2["Kumulative Häufigkeit"] = df2["Relative Häufigkeit"].cumsum()  # F(x)

    print("Aufgabe 1 Häufigkeitstabelle")

    # Varianz
    x = 0
    arithmetisches_mittel = 0
    for y in range(6):
        arithmetisches_mittel += (df2["Absolute Häufigkeit"][y] * df2["Klassenmitte"][y])

    arithmetisches_mittel = arithmetisches_mittel / df2["Absolute Häufigkeit"].sum()
    
    for i in range(6):
        x += df2["Absolute Häufigkeit"][i] * (df2["Klassenmitte"][i] - arithmetisches_mittel)**2 
    varianz_haeufigkeitstabelle = x / df2["Absolute Häufigkeit"].sum()
    print(f"\nVarianz aus Häufigkeitstabelle: {varianz_haeufigkeitstabelle:.2f}")

    std_haeufigkeitstabelle = varianz_haeufigkeitstabelle**0.5
    print(f"Standardabweichung aus Häufigkeitstabelle: {std_haeufigkeitstabelle:.2f}\n")


    # Aufgabe 2
    # Berechnen Sie für das Merkmal Studiendauer aus der Aufgabe 1 des Aufgabenblatts 2:
    # • Varianz und Standardabweichung

    data3 = {
        "G":  [1,1,1,1,1,1,2,2,1,2,1,1,2,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,2,2],
        "S":  [12,13,12,12,9,12,14,10,18,10,13,15,13,16,14,13,13,17,12,15,13,13,15,13,15,12,14,10,12,17,11,14,11,13,11,7],
        "E":  [1,3,5,2,3,2,5,1,3,3,4,4,2,3,3,2,2,1,2,2,3,4,1,3,4,2,1,2,3,2,1,3,2,2,3,1],
        "D":  [3,4,4,3,4,1,3,4,3,4,4,3,2,3,4,3,4,4,2,3,4,3,4,2,4,4,3,4,3,3,4,2,1,4,4,4],
        "N":  [2,2,3,3,2,1,5,2,1,3,3,2,2,2,2,2,2,3,2,3,2,3,2,2,3,2,2,2,2,2,2,3,2,3,3,2],
    }

    df3 = pd.DataFrame(data3)
    print("Aufgabe 2")

    varianz_Studiendauer = df3["S"].var(ddof=0)
    std_Studiendauer = varianz_Studiendauer**0.5

    print(f"Varianz Studiendauer: {varianz_Studiendauer:.2f}")
    print(f"Standardabweichung Studiendauer: {std_Studiendauer:.2f}\n")

    # Aufgabe 3
    # Berechnen Sie für die Aufgaben 1 und 3 des Aufgabenblatts 3:
    # • Varianz und Standardabweichung

    # Aufgabe 1 des Aufgabenblatts 3
    data4 = {
        "Klasse": ["0-<2", "2-<4", "4-<6", "6-<8", "8-<10", "10-<15", "15-<30"],
        "Häufigkeit": [1650, 1111, 720, 508, 332, 427, 252],
        "Klassenbreite": [2, 2, 2, 2, 2, 5, 15],  
        "Klassenmitte": [1, 3, 5, 7, 9, 12.5, 22.5],  
    }

    df4 = pd.DataFrame(data4)

    df4["Relative Häufigkeit"] = df4["Häufigkeit"] / df4["Häufigkeit"].sum()
    df4["Klassendichte"] = df4["Relative Häufigkeit"] / df4["Klassenbreite"]
    df4["Kumulierte Häufigkeit"] = df4["Relative Häufigkeit"].cumsum()
    print("Aufgabe 3/1")

    z = 0
    arithmetisches_mittel2 = 0
    for z in range(7):
        arithmetisches_mittel2 += (df4["Häufigkeit"][z] * df4["Klassenmitte"][z])

    arithmetisches_mittel2 = arithmetisches_mittel2 / df4["Häufigkeit"].sum()
    y = 0
    for i in range(7):
        y += df4["Häufigkeit"][i] * (df4["Klassenmitte"][i] - arithmetisches_mittel2)**2

    varianz_a1 = y / 5000
    print(f"\nVarianz aus Häufigkeitstabelle: {varianz_a1:.2f}")

    std_a1 = varianz_a1**0.5
    print(f"Standardabweichung aus Häufigkeitstabelle: {std_a1:.2f}\n")

    # Aufgabe 3 des Aufgabenblatts 3
    data5 = {
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
    df5 = pd.DataFrame(data5)
    print("Aufgabe 3/3")

    arithmetisches_mittel3 = 0
    for p in range(6):
        arithmetisches_mittel3 += df5["n NRW"][p] * df5["Klassenmitten"][p]
    arithmetisches_mittel3 = arithmetisches_mittel3 / df5["n NRW"].sum()
    z = 0
    for i in range(6):
        z += df5["n NRW"][i] * (df5["Klassenmitten"][i] - arithmetisches_mittel3)**2

    varianz_a3_NRW = z / df5["n NRW"].sum()
    print(f"\nVarianz aus Häufigkeitstabelle NRW: {varianz_a3_NRW:.2f}")

    std_a3_NRW = varianz_a3_NRW**0.5
    print(f"Standardabweichung aus Häufigkeitstabelle NRW: {std_a3_NRW:.2f}\n")


    arithmetisches_mittel4 = 0
    for i in range(6):
        arithmetisches_mittel4 += df5["n BY"][i] * df5["Klassenmitten"][i]

    arithmetisches_mittel4 = arithmetisches_mittel4 / df5["n BY"].sum()

    z2 = 0
    for i in range(6):
        z2 += df5["n BY"][i] * (df5["Klassenmitten"][i] -arithmetisches_mittel4)**2
    varianz_a3_BY = z2 / df5["n BY"].sum()
    print(f"\nVarianz aus Häufigkeitstabelle BY: {varianz_a3_BY:.2f}")
    std_a3_BY = varianz_a3_BY**0.5
    print(f"Standardabweichung aus Häufigkeitstabelle BY: {std_a3_BY:.2f}\n")

    # Aufgabe 4
    # Berechnen Sie für die Aufgabe 3 des Aufgabenblatts 4:
    # • Berechnen Sie näherungsweise das arithmetische Mittel aus der Klassierung.
    # • Berechnen Sie näherungsweise die Varianz und die Standardabweichung.

    werte = [8, 0, 17, 12, 22, 3, 5, 52, 1, 42, 8, 12, 10, 19, 21, 6, 5, 33, 36, 6]
    klassen = ["0-<10", "10-<20", "20-<30", "30-<40", "40-<52"]

    # Klassenbreite berechnen
    bins = [0, 10, 20, 30, 40, 52]  # Klassenränder
    dfx = pd.cut(werte, bins=bins, right=False).value_counts().sort_index()

    # DataFrame erstellen
    data6 = {
        "Klasse": klassen,
        "Häufigkeit": dfx.values,
        "Klassenbreite": [10, 10, 10, 10, 12],
        "Klassenmitte": [5, 15, 25, 35, 46],
    }

    df6 = pd.DataFrame(data6)

    df6["Relative Häufigkeit"] = df6["Häufigkeit"] / df6["Häufigkeit"].sum()
    df6["Klassendichte"] = df6["Relative Häufigkeit"] / df6["Klassenbreite"]
    df6["Kumulative Häufigkeit"] = df6["Relative Häufigkeit"].cumsum()
    print("Aufgabe 4")

    # arithmetisches Mittel
    arithmetisches_mittel_a4 = (df6["Klassenmitte"] * df6["Relative Häufigkeit"]).sum()
    print(f"\nArithmetisches Mittel: {arithmetisches_mittel_a4:.2f}")

    # Varianz
    varianz_a4 = 0
    for i in range(5):
        varianz_a4 += df6["Häufigkeit"][i] * (df6["Klassenmitte"][i] - arithmetisches_mittel_a4)**2
    varianz_a4 /= 5
    print(f"Varianz: {varianz_a4:.2f}")

    # Standardabweichung
    std_a4 = varianz_a4**0.5
    print(f"Standardabweichung: {std_a4:.2f}\n")

    # Aufgabe 5
    # Berechnen Sie für die Aufgabe 5:
    # • Modus, Median, Arithmetisches Mittel, Standardabweichung und Variationskoeffizient

    data7 = {
        "Alter": [35, 39, 43, 46, 50, 54],
        "Besucher Vortrag 1": [4, 8, 4, 2, 1, 0],
        "Besucher Vortrag 2": [0, 3, 6, 5, 4, 3],
    }

    # DataFrame erstellen
    df7 = pd.DataFrame(data7)

    # Modus
    modus_v1 = df7.loc[df7["Besucher Vortrag 1"].idxmax(), "Alter"]
    modus_v2 = df7.loc[df7["Besucher Vortrag 2"].idxmax(), "Alter"]

    # Median
    median_v1 = np.repeat(df7["Alter"], df7["Besucher Vortrag 1"]).median()
    median_v2 = np.repeat(df7["Alter"], df7["Besucher Vortrag 2"]).median()

    # Arithmetisches Mittel
    arith_mittel_v1 = (df7["Alter"] * df7["Besucher Vortrag 1"]).sum() / df7["Besucher Vortrag 1"].sum()
    arith_mittel_v2 = (df7["Alter"] * df7["Besucher Vortrag 2"]).sum() / df7["Besucher Vortrag 2"].sum()

    # Standardabweichung
    std_v1 = np.sqrt(((df7["Alter"] - arith_mittel_v1)**2 * df7["Besucher Vortrag 1"]).sum() / df7["Besucher Vortrag 1"].sum())
    std_v2 = np.sqrt(((df7["Alter"] - arith_mittel_v2)**2 * df7["Besucher Vortrag 2"]).sum() / df7["Besucher Vortrag 2"].sum())

    # Variationskoeffizient
    var_koeff_v1 = std_v1 / arith_mittel_v1
    var_koeff_v2 = std_v2 / arith_mittel_v2

    # Ergebnisse ausgeben
    print(f"Vortrag 1:")
    print(f"Modus: {modus_v1}")
    print(f"Median: {median_v1}")
    print(f"Arithmetisches Mittel: {arith_mittel_v1:.2f}")
    print(f"Variationskoeffizient: {var_koeff_v1:.2f}\n")

    print(f"Vortrag 2:")
    print(f"Modus: {modus_v2}")
    print(f"Median: {median_v2}")
    print(f"Arithmetisches Mittel: {arith_mittel_v2:.2f}")
    print(f"Variationskoeffizient: {var_koeff_v2:.2f}")

    sys.stdout = sys.__stdout__  # Zurücksetzen der Standardausgabe

# PDF erstellen
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Ausgabe in die PDF schreiben
with open("output_Übungsblatt5.txt", "r") as f:
    for line in f:
        pdf.cell(200, 10, txt=line, ln=True)

# PDF speichern
pdf.output("output_Übungsblatt5.pdf")

os.remove("output_Übungsblatt5.txt")