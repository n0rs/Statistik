import pandas as pd
import Berechnungssfunktionen as bf
import sys
import os
from fpdf import FPDF



with open("Übungsblatt8.txt", "w") as f:
    sys.stdout = f
    # Hier das gesamte Skript ausführen
    print("Übungsblatt8:")

    data = {
        "Studienjahr": ["1. Studienjahr", "2. Studienjahr", "3. Studienjahr", "4. Studienjahr", "Gesamt"],
        "In Köln": [13, 9, 8, 15, 45],  # Personen, die in Köln wohnen
        "Nicht in Köln": [27, 26, 37, 15, 105],  # Personen, die nicht in Köln wohnen
        "Gesamt": [40, 35, 45, 30, 150]  # Gesamtsumme pro Studienjahr
    }

    df = pd.DataFrame(data)

    chi_quadrat = bf.chi_quadrat_wert(df["In Köln"].values, df["Nicht in Köln"].values)
    print(f"Chi Quadrat Wert der Merkmale: {chi_quadrat}")

    cramer_v = bf.cramer_v_wert(chi_quadrat, df[["In Köln", "Nicht in Köln"]])
    print(f"Cramers V: {cramer_v:.4f}")

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Ausgabe in die PDF schreiben
with open("Übungsblatt8.txt", "r") as f:
    for line in f:
        pdf.cell(200, 10, txt=line, ln=True)


pdf.output("Übungsblatt8.pdf")
os.remove("Übungsblatt8.txt")
