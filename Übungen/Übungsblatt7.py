import pandas as pd
import Berechnungssfunktionen as bf
import sys
import os
from fpdf import FPDF



with open("Übungsblatt7.txt", "w") as f:
    sys.stdout = f
    # Hier das gesamte Skript ausführen
    print("Übungsblatt7:")

    # Daten der Kontingenztabelle
    data = {
        "Rauchverhalten": ["Starker Raucher", "Mäßiger Raucher", "Nichtraucher"],
        "männlich": [300, 50, 150],
        "weiblich": [600, 100, 30]
    }

    # DataFrame erstellen
    df = pd.DataFrame(data)

    print("\nAufgabe 2.1")
    # Zeilen-Randverteilungen hinzufügen
    df["Gesamt"] = df[["männlich", "weiblich"]].sum(axis=1)

    # Spalten-Randverteilungen hinzufügen
    df.loc["Gesamt"] = df[["männlich", "weiblich", "Gesamt"]].sum()
    df.loc["Gesamt", "Rauchverhalten"] = "Gesamt"

    # DataFrame ohne Index ausgeben
    print(df.to_string(index=False))

    print("\nAufgabe 2.2")
    # Absolute Häufigkeiten für männlich
    abs_haeufigkeiten = df["männlich"][:-1]  # Ohne die Zeile "Gesamt"

    # Relative Häufigkeiten für männlich
    rel_haeufigkeiten = abs_haeufigkeiten / abs_haeufigkeiten.sum()

    # Häufigkeitstabelle erstellen
    haeufigkeitstabelle = pd.DataFrame({
        "Rauchverhalten": df["Rauchverhalten"][:-1],  # Ohne die Zeile "Gesamt"
        "Absolute Häufigkeit": abs_haeufigkeiten,
        "Relative Häufigkeit": rel_haeufigkeiten
    })

    # Häufigkeitstabelle anzeigen
    print("Häufigkeitstabelle (männlich):")
    print(haeufigkeitstabelle.to_string(index=False))

    print("\nAufgabe 2.3")

    chi_quadrat = bf.chi_quadrat_wert(df["männlich"].values, df["weiblich"].values)
    print(f"Chi Quadrat Wert der Merkmale: {chi_quadrat}")


    print("\nAufgabe 3")

    # Neue Kontingenztabelle
    data2 = {
        "Studienjahr": ["1. Studienjahr", "2. Studienjahr", "3. Studienjahr", "4. Studienjahr", "Gesamt"],
        "In Köln": [0, 9, 8, 15, 32],  # Personen, die in Köln wohnen
        "Nicht in Köln": [40, 26, 0, 15, 81],  # Personen, die nicht in Köln wohnen
        "Gesamt": [40, 35, 8, 30, 150]  # Gesamtsumme pro Studienjahr
    }

    df2 = pd.DataFrame(data2)
    print(df2.to_string(index=False))

    chi_quadrat2 = bf.chi_quadrat_wert(df2["In Köln"].values, df2["Nicht in Köln"].values)
    print(f"Chi Quadrat Wert der Merkmale: {chi_quadrat2}")

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Ausgabe in die PDF schreiben
with open("Übungsblatt7.txt", "r") as f:
    for line in f:
        pdf.cell(200, 10, txt=line, ln=True)


pdf.output("Übungsblatt7.pdf")
os.remove("Übungsblatt7.txt")
