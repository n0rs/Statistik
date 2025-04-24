import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import Berechnungssfunktionen as bf
import sys
import scipy.stats
from fpdf import FPDF
import os

# Aufgabe 2
with open("output_Übungsblatt6.txt", "w") as f:
    sys.stdout = f
    # Hier das gesamte Skript ausführen
    print("Ausgabe von Übungsblatt5:")

    data = {
        "Brauerei": ["Warsteiner", "Bitburger", "Krombacher", "Holsten", "Veltins", "König", "Paulaner", "Henninger", "Licher"],
        "pi": [5534, 3375, 3060, 2700, 2120, 2107, 1900, 1751, 1605],
        "wi": [24.6, 20.4, 25.1, 23.3, 16.8, 17.4, 9.1, 10.0, 11.5],
        "rang_pi" : [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "rang_wi" : [1, 4, 2, 3, 6, 5, 9, 8, 7]
    }


    print("""
        Statistische Einheit:
        Sachverhalt: Im gegebenen Beispiel ist jede Bierbrauerei eine statistische Einheit, da für jede \n    Brauerei der Produktionsausstoß und der Werbeaufwand erhoben werden.\n
        Statistische Gesamtheit:
        Sachverhalt: Die Gesamtheit der neun größten Bierbrauereien Deutschlands bildet die statistische Gesamtheit.\n
        Erhebungsmerkmale:
        Sachverhalt: Die Erhebungsmerkmale sind:
        Produktionsausstoß ( P ) (in 1000 hl)
        Werbeaufwand ( W ) (in Mio. Euro)\n
        Skala:
        Sachverhalt:
        Der Produktionsausstoß ( P ) und der Werbeaufwand ( W ) sind metrisch skalierte Merkmale,\n    da sie in Zahlenwerten gemessen werden und arithmetische Operationen (z. B. Mittelwert) sinnvoll sind.
    """)

    df = pd.DataFrame(data)

    # Aufgabe 1/2
    print("\nAufgabe 1/2\n")
    chi_quadrat = bf.chi_quadrat_wert(df["pi"], df["wi"])
    print(f"Chi-Quadrat: {chi_quadrat:.4f}")

    phi_koeffizient = bf.phi_koeffizient_wert(chi_quadrat, df[["pi", "wi"]])
    print(f"Phi-Koeffizient: {phi_koeffizient:.4f}")

    kontingenzkoeffizient = bf.kontingenzkoeffizient_wert(chi_quadrat, df[["pi", "wi"]])
    print(f"Kontingenzkoeffizient: {kontingenzkoeffizient:.4f}")

    cramer_v = bf.cramer_v_wert(chi_quadrat, df[["pi", "wi"]])
    print(f"Cramers V: {cramer_v:.4f}")

    rangkorrelation = bf.rangkorrelation_wert_spearman([df["rang_pi"], df["rang_wi"]])
    print(f"Rangkorrelation: {rangkorrelation:.4f}")


    # Aufgabe 1/3
    print("\nAufgabe 1/3\n")
    sns.regplot(data=df, x="pi", y="wi", ci=None)
    plt.title("Scatterplot mit Regressionsgerade")
    plt.xlabel("Produktionsausstoß (in 1000 hl)")
    plt.ylabel("Werbeaufwand (in Mio. Euro)")
    plt.savefig("scatterplot_regression.png")
    plt.close()

    # Aufgabe 2

    # Daten
    data2 = {
        "Proband": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "X": [43, 47, 52, 54, 56, 58, 60, 68, 69, 72, 83, 84],
        "Y": [3.0, 1.2, 4.2, 4.0, 4.3, 6.6, 2.8, 5.9, 4.1, 4.8, 9.2, 5.0],
        "Rang_X": [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "Rang_Y": [10, 12, 7, 9, 6, 2, 7, 11, 8, 5, 1, 4]
    }

    df2 = pd.DataFrame(data2)
    print("\nAufgabe 2\n")

    spearman_korrelation = df2["X"].corr(df2["Y"], method="spearman")
    print(f"Spearman-Korrelation: {spearman_korrelation}")

    spearman_korrelation3 = scipy.stats.spearmanr(df2["X"], df2["Y"])
    print(spearman_korrelation3[0])

    pearson_korrelation = df2["X"].corr(df2["Y"], method="pearson")
    print(f"Pearson-Korrelation: {pearson_korrelation:.4f}")
    print("Es besteht ein positiver linearer Zusammenhang zwischen den Variablen X und Y,\nda die Korrelationen positiv sind.\n")


    # Aufgabe 3
    data3 = {
        "i": [1, 2, 3, 4, 5, 6],
        "x": [1.8, 1.72, 1.76, 1.85, 1.69, 1.88],
        "z": [10.46, 10.54, 10.46, 10.4, 10.52, 10.31],
        "rang_x": [4, 2, 3, 5, 1, 6],
        "rang_z": [3, 5, 4, 2, 6, 1]
    }

    df3 = pd.DataFrame(data3)
    print("\nAufgabe 3\n")

    chi_quadrat2 = bf.chi_quadrat_wert(df3["x"], df3["z"])
    print(f"Chi-Quadrat: {chi_quadrat2:.4f}")
    
    kontingenzkoeffizient2 = bf.kontingenzkoeffizient_wert(chi_quadrat2, df3[["x", "z"]])
    print(f"Kontingenzkoeffizient: {kontingenzkoeffizient2:.4f}")

    spearman_korrelation2 = df3["x"].corr(df3["z"], method="spearman")
    print(f"Spearman-Korrelation: {spearman_korrelation2:.4f}")

    sns.regplot(data=df3, x="x", y="z", ci=None)
    plt.title("Scatterplot der Variablen Größe und Zeit")
    plt.xlabel("Größe (in m)")
    plt.ylabel("Zeit (in s)")
    plt.savefig("scatterplot_zeit.png")
    plt.close()


pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Ausgabe in die PDF schreiben
with open("output_Übungsblatt6.txt", "r") as f:
    for line in f:
        pdf.cell(200, 10, txt=line, ln=True)

pdf.add_page()
pdf.image("scatterplot_regression.png", x=10, y=15, w=180)
pdf.add_page()
pdf.image("scatterplot_zeit.png", x=10, y=15, w=180)
pdf.output("output_Übungsblatt6.pdf")
os.remove("output_Übungsblatt6.txt")
os.remove("scatterplot_regression.png")
os.remove("scatterplot_zeit.png")







