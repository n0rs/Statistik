def arith_mittel(häufigkeit, klassenmitte):
    z = 0
    for i in range(häufigkeit.count()):
        z += (häufigkeit[i] * klassenmitte[i])
    z = z / häufigkeit.sum()
    return z

def var_wert(häufigkeit, klassenmitte, arith_mittel):
    z = 0
    for i in range(häufigkeit.count()):
        z += häufigkeit[i] * (klassenmitte[i] - arith_mittel)**2
    z = z / häufigkeit.sum()
    return z

def std_wert(varianz):
    std = varianz**0.5
    return std

def mod_wert(häufigkeit, klassenmitte):
    return klassenmitte.loc[häufigkeit.idxmax()]

def unteres_quartil_wert(quartilwert, klassendichte, klasse, klassen_spalte):
    index = klassen_spalte[klassen_spalte == klasse].index
    return quartilwert / klassendichte.loc[index].values[0]

#def mittleres_quartil_wert(kumulierte_haeufigkeit, klassendichte, klasse, quartilwert=0.5):
#    kumulierte_haeufigkeit = pd.to_numeric(kumulierte_haeufigkeit, errors='coerce')
#
 #   untere_grenze = float(klasse.split("-<")[0])

 #   vorherige_kumulierte_haeufigkeit = kumulierte_haeufigkeit[kumulierte_haeufigkeit < quartilwert].values[-1]


  #  dichte = klassendichte.loc[klassendichte.index[klassendichte.index == klasse]].values[0]

   # return untere_grenze + (quartilwert - vorherige_kumulierte_haeufigkeit) / dichte
