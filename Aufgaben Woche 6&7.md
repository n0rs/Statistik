
## **Aufgabe 1 (2×3-Kontingenztabelle):**

In einer Firma arbeiten 90 Personen: 30 in der Produktion, 25 in der Verwaltung und 35 im Außendienst. 15 Personen aus der Produktion sind Männer, 10 der Verwaltungsmitarbeiter sind Männer, und 20 der Außendienstmitarbeiter sind Frauen.

**Aufgaben:**

1. Erstellen Sie eine $2 \times 3$-Kontingenztabelle (Geschlecht × Abteilung).
    
2. Untersuchen Sie die beiden Merkmale auf statistische Unabhängigkeit.
    
3. Berechnen Sie dazu den $χ2$-Wert.
    



**Lösung zu Aufgabe 1:**

**1. Kontingenztabelle:**

|Geschlecht|Produktion|Verwaltung|Außendienst|Summe|
|---|---|---|---|---|
|Männer|15|10|15|40|
|Frauen|15|15|20|50|
|**Summe**|30|25|35|90|

---

**2. Erwartete Häufigkeiten berechnen:**

$E_{ij} = \frac{(Zeilensumme_i) \cdot (Spaltensumme_j)}{Gesamtsumme}$

Beispiel: Erwartete Männer in Produktion:

$E = \frac{40 \cdot 30}{90} = \frac{1200}{90} = 13.\overline{3}$

Alle Erwartungswerte:

|Geschlecht|Produktion|Verwaltung|Außendienst|
|---|---|---|---|
|Männer|13.33|11.11|15.56|
|Frauen|16.67|13.89|19.44|

---

**3. $χ2$-Berechnung:**

$\chi^2 = \sum \frac{(O - E)^2}{E}$

Berechnung:

- $Produktion Männer: \frac{(15 - 13.33)^2}{13.33} = 0.208$
    
- $Produktion Frauen: \frac{(15 - 16.67)^2}{16.67} = 0.167$
    
- $Verwaltung Männer: \frac{(10 - 11.11)^2}{11.11} = 0.111$
    
- $Verwaltung Frauen: \frac{(15 - 13.89)^2}{13.89} = 0.087$
    
- $Außendienst Männer: \frac{(15 - 15.56)^2}{15.56} = 0.020$
    
- $Außendienst Frauen: \frac{(20 - 19.44)^2}{19.44} = 0.016$
    

$χ2≈0.208+0.167+0.111+0.087+0.020+0.016=0.609$


## **Aufgabe 2 (2×4-Kontingenztabelle):**

In einer Schule gibt es 120 Schüler: 40 in Klasse 5, 30 in Klasse 6, 25 in Klasse 7 und 25 in Klasse 8. 20 der Schüler in Klasse 5 besuchen die Nachmittagsbetreuung, 10 der Schüler in Klasse 6 tun das ebenfalls. In Klasse 7 sind 15 Jungen, davon 9 besuchen die Nachmittagsbetreuung. In Klasse 8 besuchen 5 Mädchen die Nachmittagsbetreuung. Insgesamt nehmen 45 Schüler an der Nachmittagsbetreuung teil, davon 30 Jungen.

**Aufgaben:**

1. Erstellen Sie eine $2 \times 4$-Kontingenztabelle (Nachmittagsbetreuung × Klassenstufe).
    
2. Prüfen Sie auf Unabhängigkeit.
    
3. Berechnen Sie $χ2$.
    

---

**Lösung zu Aufgabe 2:**

**1. Bestimmung aller Werte:**

- Klasse 5: 20 Ja → 20 Nein
    
- Klasse 6: 10 Ja → 20 Nein
    
- Klasse 7: 9 Ja → 16 Nein (25 - 9)
    
- Klasse 8: 6 Ja (weil: 45 - (20 + 10 + 9) = 6) → 19 Nein
    

**Kontingenztabelle:**

| Betreuung | Klasse 5 | Klasse 6 | Klasse 7 | Klasse 8 | Summe |
| --------- | -------- | -------- | -------- | -------- | ----- |
| Ja        | 20       | 10       | 9        | 6        | 45    |
| Nein      | 20       | 20       | 16       | 19       | 75    |
| **Summe** | 40       | 30       | 25       | 25       | 120   |

---

**2. Erwartete Häufigkeiten:**

Beispiel: Erwartet „Ja“ in Klasse 5:

$E = \frac{45 \cdot 40}{120} = 15$

Erwartungswerte „Ja“:

- Klasse 5: 15
    
- Klasse 6: 11.25
    
- Klasse 7: 9.375
    
- Klasse 8: 9.375
    

Erwartungswerte „Nein“ = Spaltensumme − Erwartung „Ja“

---

**3. $\chi^2$:**

Berechnung:

- $(20−15)²/15 = 1.667$
    
- $(10−11.25)²/11.25 = 0.139$
    
- $(9−9.375)²/9.375 = 0.015$
    
- $(6−9.375)²/9.375 = 1.215$
    
- $(20−25)²/25 = 1.0$
    
- $(20−18.75)²/18.75 = 0.083$
    
- $(16−15.625)²/15.625 = 0.00$9
    
- $(19−15.625)²/15.625 = 0.722$
    

$\chi^2 \approx 1.667 + 0.139 + 0.015 + 1.215 + 1.0 + 0.083 + 0.009 + 0.722 = \boxed{4.85}$



## Aufgabe 3 – (2×3-Kontingenztabelle)

In einer Befragung zur Nutzung von Streamingdiensten wurden 180 Personen nach ihrem Alter und ihrer bevorzugten Streamingplattform befragt. Die Altersgruppen sind **"unter 30"** und **"30 oder älter"**. Die Plattformen sind **Netflix**, **Disney+** und **Amazon Prime**.  
Die Ergebnisse sind:

|Alter|Netflix|Disney+|Amazon Prime|Summe|
|---|---|---|---|---|
|unter 30|40|30|20|90|
|30 oder älter|20|10|60|90|
|**Summe**|60|40|80|180|

### Aufgabenstellung:

1. Geben Sie die beiden **Randverteilungen** (Zeilen- und Spaltensummen) an.
    
2. Geben Sie für die Verteilung der **Streamingpräferenz unter der Bedingung „unter 30“** eine Häufigkeitstabelle mit absoluten und relativen Häufigkeiten an.
    
3. **Berechnen Sie den** χ2-**Wert** zur Überprüfung der Unabhängigkeit.
    

---

###  Lösung zu Aufgabe 3:

#### 1. Randverteilungen:

- **Zeilensummen:**
    
    - unter 30: 90
        
    - 30 oder älter: 90
        
- **Spaltensummen:**
    
    - Netflix: 60
        
    - Disney+: 40
        
    - Prime: 80
        

#### 2. Bedingte Verteilung: Alter < 30

|Plattform|absolute Häufigkeit|relative Häufigkeit|
|---|---|---|
|Netflix|40|40/90 = 0.444|
|Disney+|30|30/90 = 0.333|
|Amazon Prime|20|20/90 = 0.222|

#### 3. Erwartete Häufigkeiten

$E_{ij} = \frac{\text{Zeilensumme}_i \cdot \text{Spaltensumme}_j}{\text{Gesamtsumme}}$

Beispiel:

$E_{\text{unter30, Netflix}} = \frac{90 \cdot 60}{180} = 30$

|Alter|Netflix|Disney+|Prime|
|---|---|---|---|
|unter 30|30|20|40|
|30 oder älter|30|20|40|

#### χ2-Berechnung:

$\chi^2 = \sum \frac{(O - E)^2}{E} = \frac{(40 - 30)^2}{30} + \frac{(30 - 20)^2}{20} + \frac{(20 - 40)^2}{40} \\ + \frac{(20 - 30)^2}{30} + \frac{(10 - 20)^2}{20} + \frac{(60 - 40)^2}{40}$ 
$\chi^2 = \frac{100}{30} + \frac{100}{20} + \frac{400}{40} + \frac{100}{30} + \frac{100}{20} + \frac{400}{40} = 3.33 + 5 + 10 + 3.33 + 5 + 10 = \boxed{36.67}$



## Aufgabe 4 – (2×4-Kontingenztabelle)

Im Rahmen einer Untersuchung zur Mediennutzung wurden 200 Personen befragt, wie häufig sie Tageszeitungen lesen.  
Die Personen wurden nach **Bildungsabschluss** (Abitur / kein Abitur) und nach **Lesehäufigkeit** (täglich, mehrmals pro Woche, selten, nie) klassifiziert.

|Bildung|täglich|mehrmals/Woche|selten|nie|Summe|
|---|---|---|---|---|---|
|Abitur|20|30|40|10|100|
|Kein Abitur|10|20|50|20|100|
|**Summe**|30|50|90|30|200|

### Aufgabenstellung:

1. Geben Sie die **Randverteilungen** an.
    
2. Geben Sie für die Verteilung der **Lesehäufigkeit unter der Bedingung „Abitur“** eine Tabelle mit absoluten und relativen Häufigkeiten an.
    
3. **Berechnen Sie den** χ2-**Wert** zur Überprüfung der Unabhängigkeit.
    

---

### Lösung zu Aufgabe 4:

#### 1. Randverteilungen:

- **Zeilensummen:**
    
    - Abitur: 100
        
    - Kein Abitur: 100
        
- **Spaltensummen:**
    
    - Täglich: 30
        
    - Mehrmals/Woche: 50
        
    - Selten: 90
        
    - Nie: 30
        

#### 2. Bedingte Verteilung: Abitur

|Lesehäufigkeit|absolute|relative|
|---|---|---|
|täglich|20|0.20|
|mehrmals/Woche|30|0.30|
|selten|40|0.40|
|nie|10|0.10|

#### 3. Erwartete Häufigkeiten

$E_{\text{Abitur, täglich}} = \frac{100 \cdot 30}{200} = 15$

| Bildung     | täglich | mehrmals | selten | nie |
| ----------- | ------- | -------- | ------ | --- |
| Abitur      | 15      | 25       | 45     | 15  |
| Kein Abitur | 15      | 25       | 45     | 15  |

#### χ2-Berechnung:

$\chi^2 = \sum \frac{(O - E)^2}{E} = \frac{(20 - 15)^2}{15} + \frac{(30 - 25)^2}{25} + \frac{(40 - 45)^2}{45} + \frac{(10 - 15)^2}{15} \\ + \frac{(10 - 15)^2}{15} + \frac{(20 - 25)^2}{25} + \frac{(50 - 45)^2}{45} + \frac{(20 - 15)^2}{15}$ $\chi^2 = \frac{25}{15} + \frac{25}{25} + \frac{25}{45} + \frac{25}{15} + \frac{25}{15} + \frac{25}{25} + \frac{25}{45} + \frac{25}{15} = \boxed{9.8}$



## Aufgabe 5 – 2×3 Kontingenztabelle (Textaufgabe mit Cramérs V)

**Thema:** Sportverhalten nach Studienfach  
**Stichprobe:** 180 Studierende (90 Technik, 90 Wirtschaft)  
**Merkmale:**

- **Sportverhalten:** regelmäßig, gelegentlich, nie
    
- **Fachbereich:** Technik, Wirtschaft
    

**Ergebnisse:**

|Fachbereich|regelmäßig|gelegentlich|nie|Summe|
|---|---|---|---|---|
|Technik|30|40|20|90|
|Wirtschaft|20|30|40|90|
|**Summe**|50|70|60|180|

###  Aufgabenstellung

1. Erstellen Sie die vollständige Kontingenztabelle.
    
2. Geben Sie die Randverteilungen an.
    
3. Erstellen Sie die bedingte Verteilung des Sportverhaltens unter der Bedingung „Wirtschaft“.
    
4. Berechnen Sie den χ2-Wert.
    
5. Berechnen Sie Cramérs V zur Bewertung der Stärke des Zusammenhangs.
    

---

### Lösung zu Aufgabe 5

#### 1. Randverteilungen

- **Zeilen:**
    
    - Technik: 90
        
    - Wirtschaft: 90
        
- **Spalten:**
    
    - regelmäßig: 50
        
    - gelegentlich: 70
        
    - nie: 60
        

#### 2. Bedingte Verteilung (Wirtschaft)

|Sportverhalten|absolut|relativ|
|---|---|---|
|regelmäßig|20|0.222|
|gelegentlich|30|0.333|
|nie|40|0.444|

#### 3. Erwartete Häufigkeiten

Formel:

$E_{ij} = \frac{\text{Zeilensumme}_i \cdot \text{Spaltensumme}_j}{n}$

E$_{\text{Technik, regelmäßig}} = \frac{90 \cdot 50}{180} = 25$

| Kategorie              | O   | E   | $\frac{(O - E)^2}{n}$ |
| ---------------------- | --- | --- | --------------------- |
| Technik, regelmäßig    | 30  | 25  | 1.000                 |
| Technik, gelegentlich  | 40  | 35  | 0.714                 |
| Technik, nie           | 20  | 30  | 3.333                 |
| Wirtschaft, regelmäßig | 20  | 25  | 1.000                 |
| Wirtschaft, gelegentl. | 30  | 35  | 0.714                 |
| Wirtschaft, nie        | 40  | 30  | 3.333                 |

$\chi^2 = 1 + 0.714 + 3.333 + 1 + 0.714 + 3.333 = \boxed{10.094}$

#### 4. Cramérs V

Formel:

$V = \sqrt{ \frac{10.094}{180 \cdot (3 - 1)} } = \sqrt{ \frac{10.094}{360} } \approx \sqrt{0.028} = \boxed{0.167}$

**Interpretation:** Schwacher Zusammenhang zwischen Fachbereich und Sportverhalten.

---

## Aufgabe 6 – 2×4 Kontingenztabelle (direkt gegeben, mit Cramérs V)

**Thema:** Internetnutzung nach Geschlecht  
**Stichprobe:** 200 Personen  
**Merkmale:**

- **Nutzung pro Tag:** <1 h, 1–3 h, 4–6 h, >6 h
    
- **Geschlecht:** männlich, weiblich
    

**Ergebnisse:**

|Geschlecht|<1 h|1–3 h|4–6 h|>6 h|Summe|
|---|---|---|---|---|---|
|männlich|10|30|40|20|100|
|weiblich|30|40|20|10|100|
|**Summe**|40|70|60|30|200|

---

### 🔹 Aufgabenstellung

1. Geben Sie die Randverteilungen an.
    
2. Geben Sie die bedingte Verteilung der Internetnutzung für „weiblich“ an.
    
3. Berechnen Sie den χ2-Wert.
    
4. Berechnen Sie Cramérs V zur Bewertung des Zusammenhangs.
    

---

### Lösung zu Aufgabe 2

#### 1. Randverteilungen

- **Spalten (Nutzung):**
    
    - <1 h: 40
        
    - 1–3 h: 70
        
    - 4–6 h: 60
        
    - > 6 h: 30
        
- **Zeilen:**
    
    - männlich: 100
        
    - weiblich: 100
        

#### 2. Bedingte Verteilung (weiblich)

|Nutzung|absolut|relativ|
|---|---|---|
|<1 h|30|0.30|
|1–3 h|40|0.40|
|4–6 h|20|0.20|
|>6 h|10|0.10|

#### 3. Erwartete Häufigkeiten

Da beide Gruppen gleich groß sind, gilt:

E=100⋅Spaltensumme200=Spaltensumme2E = \frac{100 \cdot \text{Spaltensumme}}{200} = \frac{\text{Spaltensumme}}{2}

| Kategorie | O   | E   | $\frac{(O - E)^2}{E}$ |
| --------- | --- | --- | --------------------- |
| m, <1 h   | 10  | 20  | 5.000                 |
| m, 1–3 h  | 30  | 35  | 0.714                 |
| m, 4–6 h  | 40  | 30  | 3.333                 |
| m, >6 h   | 20  | 15  | 1.667                 |
| w, <1 h   | 30  | 20  | 5.000                 |
| w, 1–3 h  | 40  | 35  | 0.714                 |
| w, 4–6 h  | 20  | 30  | 3.333                 |
| w, >6 h   | 10  | 15  | 1.667                 |

$\chi^2 = 5 + 0.714 + 3.333 + 1.667 + 5 + 0.714 + 3.333 + 1.667 = \boxed{21.43}$

#### 4. Cramérs V

$V = \sqrt{ \frac{\chi^2}{n(k - 1)} } = \sqrt{ \frac{21.43}{200 \cdot 3} } = \sqrt{0.0357} = \boxed{0.189}$

**Interpretation:** Leicht erhöhter, aber noch schwacher Zusammenhang zwischen Geschlecht und Internetnutzung.



# Aufgabe 7: Zufallsexperiment „Zweimaliges Werfen eines Würfels“

### **Ergebnismenge (Ω)**  
Alle geordneten Paare \( (x, y) \), wobei \( x, y \in \{1, 2, 3, 4, 5, 6\} \).  
$$
\Omega = \{(1,1), (1,2), ..., (6,6)\} \quad \text{(insgesamt 36 Elemente)}
$$


# Aufgabe 8: Zufallsexperiment „Ziehen einer Kugel aus einer Urne“

- Die Urne enthält 4 rote, 3 blaue und 2 grüne Kugeln.
- **Ergebnismenge (Ω)**:  
  $$
  \Omega = \{\text{rot}, \text{blau}, \text{grün}\}
  $$


# Aufgabe 9

Gegeben seien die Mengen  
$A = \{1, 3, 5, 7, 9\}$ und $B = \{3, 4, 5, 6\}$.

**a)** $A \cup B$  
**Lösung:**  
$A \cup B = \{1, 3, 4, 5, 6, 7, 9\}$

**b)** $A \cap B$  
**Lösung:**  
$A \cap B = \{3, 5\}$

**c)** $A \setminus B$  
**Lösung:**  
$A \setminus B = \{1, 7, 9\}$

**d)** $B \setminus A$  
**Lösung:**  
$B \setminus A = \{4, 6\}$



# Aufgabe 10

Gegeben seien die Mengen  
$C = \{a, b, c\}$ und $D = \{b, c, d, e\}$.

**a)** $C \cup D$  
**Lösung:**  
$C \cup D = \{a, b, c, d, e\}$

**b)** $C \cap D$  
**Lösung:**  
$C \cap D = \{b, c\}$

**c)** $D \setminus C$  
**Lösung:**  
$D \setminus C = \{d, e\}$

**d)** $C \setminus D$  
**Lösung:**  
$C \setminus D = \{a\}$

**e)** Wie viele Teilmengen besitzt $C$?  
**Lösung:**  
$C$ hat $3$ Elemente $\Rightarrow$ Anzahl der Teilmengen: $2^3 = 8$  
Teilmenge: $\{\}, \{a\}, \{b\}, \{c\}, \{a,b\}, \{a,c\}, \{b,c\}, \{a,b,c\}$


# Aufgabe 11: Fahrradverleihsystem in Stuttgart

Zur Analyse eines Fahrradverleihsystems in Stuttgart wird erfasst, ob ein Fahrrad
- mit einem GPS-System ausgestattet ist (Ereignis $A$),
- einen Korb besitzt (Ereignis $B$),
- über eine Gangschaltung verfügt (Ereignis $C$).

**Stellen Sie die folgenden Ereignisse durch geeignete Verknüpfungen der Ereignisse $A$, $B$, $C$ dar:**

**a)** Ein Fahrrad besitzt GPS und eine Gangschaltung  
**Lösung:** $A \cap C$

**b)** Ein Fahrrad hat zwar eine Gangschaltung, aber kein GPS  
**Lösung:** $C \cap \overline{A}$

**c)** Ein Fahrrad besitzt weder Korb noch Gangschaltung  
**Lösung:** $\overline{B} \cap \overline{C}$

**d)** Ein Fahrrad hat entweder einen Korb oder GPS, aber keine Gangschaltung  
**Lösung:** $(A \cup B) \cap \overline{C}$

**e)** Ein Fahrrad besitzt genau eine der drei Ausstattungen  
**Lösung:** $(A \cap \overline{B} \cap \overline{C}) \cup (\overline{A} \cap B \cap \overline{C}) \cup (\overline{A} \cap \overline{B} \cap C)$

---

# Aufgabe 12: Online-Bestellung in einem E-Commerce-Shop

Für die Analyse des Nutzerverhaltens eines Online-Shops wird untersucht, ob eine Bestellung
- am selben Tag geliefert wurde (Ereignis $A$),
- per Kreditkarte bezahlt wurde (Ereignis $B$),
- einen Rabattgutschein enthielt (Ereignis $C$).

**Welche Bestellungen sind durch folgende Ereignisse gekennzeichnet?**

**a)** $A \cap \overline{B}$  
**Lösung:** Bestellungen mit Same-Day-Lieferung, aber ohne Kreditkartenzahlung

**b)** $\overline{A} \cap B \cap C$  
**Lösung:** Bestellungen ohne Same-Day-Lieferung, aber mit Kreditkartenzahlung und Rabatt

**c)** $A \cup \overline{C}$  
**Lösung:** Bestellungen mit Same-Day-Lieferung oder ohne Rabatt

**d)** $C \cap \overline{(A \cup B)}$  
**Lösung:** Bestellungen mit Rabatt, aber ohne Same-Day-Lieferung und ohne Kreditkartenzahlung

**e)** $\overline{A \cup B \cup C}$  
**Lösung:** Bestellungen ohne Same-Day-Lieferung, ohne Kreditkartenzahlung und ohne Rabatt
