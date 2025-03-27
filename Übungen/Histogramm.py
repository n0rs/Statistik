import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = [1600, 2900, 3200, 4200, 2700, 2050, 3500, 2050, 2100, 2700, 2150, 1550, 1920, 2150, 3200, 2500, 1800, 1600, 2700, 5100, 2600, 6250, 2500, 2500, 2200]

# Erstelle ein Histogramm mit Seaborn und spezifischen Klassen
bins = [1500, 2000, 2500, 3000, 4000, 5000, 6500]
sns.histplot(data, bins=bins, kde=False, color='blue')

# Achsentitel und Diagrammtitel hinzufügen
plt.xlabel('Werte')
plt.ylabel('Häufigkeit')
plt.title('Histogramm der Daten mit 6 Klassen')

# Diagramm anzeigen
plt.show()