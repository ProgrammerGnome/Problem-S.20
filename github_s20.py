input_fájl = input('Please enter the name of the input file: ')
lista1 = []
forrásfájl = open(input_fájl)
for sor in forrásfájl:
    lista1.append(sor.strip().split())
lista2 = []
lista_db = []
lista2_db = []
db = 0
db2 = -1
for sor in lista1:
    for koord in sor:
        lista2.append(koord)
        db2 += 1
        db += 1
        if db%2 == 1:
            lista_db.append(db)
        if db2%2 == 0:
            lista2_db.append(db2)    
y_ok = []
x_ek = []
for szám in lista2:
    for indexelo in lista_db:
        if lista2.index(szám) == indexelo:
            y_ok.append(szám)
    for indexelo2 in lista2_db:
        if lista2.index(szám) == indexelo2:
            x_ek.append(szám)                
x_ek_int = []
y_ok_int = []
def conv(a, b):
    for i in b:
        a.append(float(i))
    return a
x_ek_int = conv(x_ek_int, x_ek)
y_ok_int = conv(y_ok_int, y_ok)
új = None
def indexkereső(szélsőértékfajta, végváltozó, db, vizsgálati_koordfajta):
    for koord in vizsgálati_koordfajta:
        db += 1
        if koord == szélsőértékfajta(vizsgálati_koordfajta):
            végváltozó = db-1
    return végváltozó
sorszám_index_min_x = indexkereső(min, új, 0, x_ek_int)
sorszám_index_max_x = indexkereső(max, új, 0, x_ek_int)
sorszám_index_min_y = indexkereső(min, új, 0, y_ok_int)
sorszám_index_max_y = indexkereső(max, új, 0, y_ok_int)
indexek = [sorszám_index_min_x,sorszám_index_max_x,sorszám_index_min_y,sorszám_index_max_y]
ideiglenes = []
def kiiro(számláló, bejárandó, i1, i2):
    for i in bejárandó:
        számláló += 1
        for j in indexek[i1:i2]:
            if j == számláló:
                ideiglenes.append(bejárandó[j])           
                break
    return bejárandó
kiiro(-1, y_ok_int, 0, 2)
kiiro(-1, y_ok_int, 2, 4)
y_ok_vissza = ideiglenes
ideiglenes = []
kiiro(-1, x_ek_int, 0, 2)
kiiro(-1, x_ek_int, 2, 4)
x_ek_vissza = ideiglenes
lista4 = []
for i in range(len(x_ek_vissza)):
    lista4.append([x_ek_vissza[i], y_ok_vissza[i]])
ymax_x = []
for i in y_ok_vissza:
    if i == max(y_ok_vissza):
        var1 = y_ok_vissza.index(max(y_ok_vissza))
        ymax_x.append(max(y_ok_vissza))
for i in x_ek_vissza:
    if x_ek_vissza.index(i) == var1:
        ymax_x.append(i)
xmax_y = []
for i in x_ek_vissza:
    if i == max(x_ek_vissza):
        var1 = x_ek_vissza.index(max(x_ek_vissza))
        xmax_y.append(max(x_ek_vissza))
for i in y_ok_vissza:
    if y_ok_vissza.index(i) == var1:
        xmax_y.append(i)
ymin_x = []
for i in y_ok_vissza:
    if i == max(y_ok_vissza):
        var1 = y_ok_vissza.index(min(y_ok_vissza))
        ymin_x.append(min(y_ok_vissza))
for i in x_ek_vissza:
    if x_ek_vissza.index(i) == var1:
        ymin_x.append(i)
xmin_y = []
for i in x_ek_vissza:
    if i == min(x_ek_vissza):
        var1 = x_ek_vissza.index(min(x_ek_vissza))
        xmin_y.append(min(x_ek_vissza))
for i in y_ok_vissza:
    if y_ok_vissza.index(i) == var1:
        xmin_y.append(i)
starter_x = xmin_y[0] #xmin
starter_y = ymax_x[0] #ymax
sz = float(starter_x-0.1)
lista_tákolmány = []
while not sz > float(xmax_y[0]):
    sz += float(0.1)
    lista_tákolmány.append(round(sz, 1))

print('... computing ...')

tavok = []
n = starter_y
while not n <= ymin_x[0]:
    n -= 1
    for i in range(len(lista_tákolmány)):
        for j in range(len(y_ok_int)):
            x1 = lista_tákolmány[i]
            x2 = x_ek_int[j]
            y1 = n
            y2 = y_ok_int[j]
            tav = round((((x1-x2)**2)+((y1-y2)**2)), 5)
            tavok.append(tav)
teszt = []
sz = 0
for i in tavok:
    sz += 1
    if sz % (len(x_ek_int)) == 0:
        teszt.append(tavok[(sz-len(x_ek_int)):sz])
fine_index_ek = []
fine_ertekek = []
for i in teszt:
    for j in i:
        fine_ertekek.append(max(i))
        fine_index_ek.append(i.index(max(i)))
        break
x = fine_ertekek.index(min(fine_ertekek))
P_k_x = []
n1 = starter_y
while not n1 <= ymin_x[0]:
    n1 -= 1
    for i in range(len(lista_tákolmány)):
        for j in range(len(y_ok_int)):
            x1 = lista_tákolmány[i]
            x2 = x_ek_int[j]
            y1 = n1
            y2 = y_ok_int[j]
            P_x = x1
            P_k_x.append(P_x)
            break
sz = -1
for i in P_k_x:
    sz += 1
    if sz == x:
        fine_x = i
P_k_x = []
n1 = starter_y
while not n1 <= ymin_x[0]:
    n1 -= 1
    for i in range(len(lista_tákolmány)):
        for j in range(len(y_ok_int)):
            x1 = lista_tákolmány[i]
            x2 = x_ek_int[j]
            y1 = n1
            y2 = y_ok_int[j]
            P_x = y1
            P_k_x.append(P_x)
            break
sz = -1
for i in P_k_x:
    sz += 1
    if sz == x:
        fine_y = i

print('A smallest circle that covers n given points in the plane: C:(x;y) = ','C:(',fine_x,';',fine_y,')',' and r=',round((min(fine_ertekek))**(1/2), 1),sep="")