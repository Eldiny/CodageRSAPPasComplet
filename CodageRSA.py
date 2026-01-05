from random import randint
from math import sqrt

def PGCD (nombreun, nombredeux) :
    a = 0
    PGCD2 = 1
    if nombreun > nombredeux :
        a = nombredeux
    else :
        a = nombreun
    for i in range(1,a+1) :
        if nombreun % i == 0 and nombredeux % i == 0 :
            PGCD2 = i
    return(PGCD2)

def Grand (nombre, N) :
    a = True
    d = 0
    while a == True :
        d = randint(1000,10000)
        if PGCD(nombre, d) == 1 :
            a = False
    return(d)

def GranbdNombresAleatoires () :
    liste = []
    d = 0
    while len(liste) < 2 :
        d = randint(1000,10000)
        if Premier(d) == True :
            liste.append(d)
    return(liste[0], liste[1])

def Premier(nombre) :
    if nombre < 2 :
        return(False)
    for i in range(2, int(sqrt(nombre)+1)) :
        if nombre % i == 0:
            return(False)
    return(True)

def CoeffDeBezout(nombreun, nombredeux) :
    if nombreun > nombredeux :
        b = nombredeux
        a = nombreun
    elif nombreun < nombredeux :
        b = nombreun
        a = nombredeux
    else :
        CoeffDeBezout(nombreun, nombredeux)
    r = 1
    u = 1
    v = 0
    x = 0
    y = 1
    while r > 0 :
        q = a//b
        r = a%b
        a,b = b,r
        u, x = x, u-(x*q)
        v, y = y, v-(q*y)
    return(u, v)

def Decoupe(mot) :
    m = 0
    dico = {}
    for n in range (97,123) :
        dico[chr(n)] = m
        m+=1
    print(dico)
    compte = 0
    verif= [chr(p) for p in range(97, 123)]
    verif2 = [chr(p) for p in range(65, 91)]
    part = ""
    liste = []
    CodeX = []
    for i in (mot) :
        for p in range(26) :
            if i == verif[p] or i == verif2[p] :
                liste += verif[p]
    for p in (liste) :
        if dico[p] < 10 :
            a = "0" + str(dico[p]) 
        else :
            a = str(dico[p])
        part += a
        compte += 1
        if compte > 2 :
            compte = 0
            CodeX.append(part)
            part = ""
    return(CodeX)

def Crypter(Code, N, e) :
    Crypté = 0
    TrucFinal = []
    for i in Code :
        Crypté = pow(int(i),e,N)
        TrucFinal.append(Crypté)
    return(TrucFinal)

def Decrypter(Code, N, d) :
    Crypté = 0
    TrucFinal = []
    for i in Code :
        Crypté = pow(int(i),d,N)
        TrucFinal.append(Crypté)
    return(TrucFinal)

p, q = GranbdNombresAleatoires()
print(p,q)
N = p*q
N2 = (p-1)*(q-1)
print(N2)
e = Grand(N2, N)
k, d = CoeffDeBezout(N2, e)
print(d)

euh = Decoupe('Bonjour a tous')
oué = (Crypter(euh, N, e))
print(euh)
print(oué)
print(Decrypter(oué, N, d))

m = 0
dico = {}
for n in range (97,123) :
    dico[chr(n)] = m
    m+=1