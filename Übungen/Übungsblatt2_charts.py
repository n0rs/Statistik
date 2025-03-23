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

# Grafiken erstellen
fig, axes = plt.subplots(3, 2, figsize=(12, 10))
fig.suptitle("Häufigkeitsverteilungen der Merkmale")

# Geschlecht
sns.countplot(x="G", data=df, ax=axes[0, 0], palette="Set2")
axes[0, 0].set_title("Geschlecht")
axes[0, 0].set_xticklabels(["weiblich", "männlich"])

# Studiendauer
sns.histplot(df["S"], bins=range(6, 20), kde=True, ax=axes[0, 1], color="blue")
axes[0, 1].set_title("Studiendauer in Semestern")

# Engagement
sns.countplot(x="E", data=df, ax=axes[1, 0], palette="Blues")
axes[1, 0].set_title("Engagement im Studium")
axes[1, 0].set_xticklabels(["sehr engagiert", "eher engagiert", "mittel", "wenig", "gar nicht"])

# Ausrichtung der Thesis
sns.countplot(x="D", data=df, ax=axes[1, 1], palette="Reds")
axes[1, 1].set_title("Ausrichtung der Bachelorthesis")
axes[1, 1].set_xticklabels(["Primärerhebung", "Sekundäranalyse", "qualitativ", "theoretisch"])

# Gesamtnote Kolloquium
sns.countplot(x="N", data=df, ax=axes[2, 0], palette="Greens")
axes[2, 0].set_title("Gesamtnote Kolloquium")
axes[2, 0].set_xticklabels(["sehr gut", "gut", "befriedigend", "ausreichend"])

# Platzhalter für leeres Feld
axes[2, 1].axis("off")

plt.tight_layout()
plt.show()
