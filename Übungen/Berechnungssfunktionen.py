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

def chi_quadrat_wert (a, b):
    x_list = []
    e_list = []
    if type(a) == "class 'pandas.core.frame.DataFrame'":
        for i in range(a.count()):
            e_list.append((a[i] + b[i]) * a.sum() / (a.sum() + b.sum()))
        for j in range(b.count()):
            e_list.append((a[j] + b[j]) * b.sum() / (a.sum() + b.sum()))
        for j in range(a.count()):
            x_list.append((a[j] - e_list[j])**2 / e_list[j])
        for j in range(b.count()):
            x_list.append((b[j] - e_list[j + len(e_list) // 2])**2 / e_list[j + len(e_list) // 2])
    else:
        for i in range(len(a)):
            e_list.append((a[i] + b[i]) * sum(a) / (sum(a) + sum(b)))
        for j in range(len(b)):
            e_list.append((a[j] + b[j]) * sum(b) / (sum(a) + sum(b)))
        for j in range(len(a)):
            x_list.append((a[j] - e_list[j])**2 / e_list[j])
        for j in range(len(b)):
            x_list.append((b[j] - e_list[j + len(e_list) // 2])**2 / e_list[j + len(e_list) // 2])
    return sum(x_list)

def phi_koeffizient_wert(chi_quadrat, häufigkeit):
    return (chi_quadrat / häufigkeit.count().sum())**0.5

def kontingenzkoeffizient_wert(chi_quadrat, häufigkeit):
    return (chi_quadrat / (chi_quadrat + häufigkeit.count().sum()))**0.5

def cramer_v_wert(chi_quadrat, häufigkeit):
    return (chi_quadrat / (häufigkeit.count().sum() * (min(häufigkeit.count()) - 1)))**0.5

def rangkorrelation_wert_spearman(ränge):
    r = []
    for i in range(ränge[0].count()):
        r.append((ränge[0][i] - ränge[1][i])**2)
    rs = 1 - (6 * sum(r) / (ränge[0].count()* (ränge[0].count()**2 - 1)))
    return rs

