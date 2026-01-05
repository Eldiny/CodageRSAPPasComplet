from random import randint
from math import sqrt

def PGCD (nombreun, nombredeux) :
    #IN : Deux nombres
    #OUT : Leur PGCD

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
    #IN : Un nombre
    #OUT : Un nommbre premier avec ce dernier
    # Tant que faux, teste des nombres aleatoires entre 1000 et 10000 jusqu'à qu'un soit premier avec le nombre

    a = True
    d = 0
    while a == True :
        d = randint(1000,10000)
        if PGCD(nombre, d) == 1 :
            a = False
    return(d)

def GranbdNombresAleatoires () :
    #IN : Rien
    #OUT : 2 nombres premiers entre 1000 et 10000
    #Teste des nombres aléatoires entre 1000 et 10000 jusqu'à en trouver 2 qui soient premiers

    liste = []
    d = 0
    while len(liste) < 2 :
        d = randint(1000,10000)
        if Premier(d) == True :
            liste.append(d)
    return(liste[0], liste[1])

def Premier(nombre) :
    #IN : Un nombre
    #OUT : La vérification de s'il est premier
    #Regarde les diviseurs jusqu'à sa racine et s'il n'y en a pas alors il est premier

    if nombre < 2 :
        return(False)
    for i in range(2, int(sqrt(nombre)+1)) :
        if nombre % i == 0:
            return(False)
    return(True)

def CoeffDeBezout(nombreun, nombredeux) :
    #IN : Deux nombres
    #OUT : Leurs coefficients de Bezout
    #Fais les trucs mathematiques bizarres pour les trouver puis les renvoie

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
    #IN : Une phrase
    #OUT : La phrase découpée en bloc de 3 maximum et retranscrite en chiffres
    #Fais un dico qui permet de retranscrir les lettres en chiffres, fais deux listes pour vérifier les lettres majuscules et minuscules et seulement ces dernieres. Puis leur attribue leurs valeurs respectivese en
    #leur rajoutant un 0 devant si nécessaire. Puis renvoie les valeurs des blocs de 3

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
    if part != "" :
        CodeX.append(part)
    return(CodeX)

def Crypter(Code, N, e) :
    #IN : Une liste et 2 nombres
    #OUT : Une liste
    #Prend le code, prend chacun des nombres à l'intérieur et les multiplie comme il faut pour les coder, puis renvoie une liste contenant les nombres codées

    Crypté = 0
    TrucFinal = []
    for i in Code :
        Crypté = pow(int(i),e,N)
        TrucFinal.append(Crypté)
    return(TrucFinal)

def Decrypter(Code, N, d) :
    #IN : Une liste et 2 nombres
    #OUT : Une liste
    #Prend le code crypté, prend chacun des nombres et leur fait l'opération pour décrypter puis les ajoute à une liste avant de la renvoyer

    Crypté = 0
    TrucFinal = []
    for i in Code :
        Crypté = pow(int(i),d,N)
        TrucFinal.append(Crypté)
    return(TrucFinal)

def Retrouve(Code) :
    #IN : Une liste
    #OUT : Une liste contenant chaque caractère décodé
    #Crée un dico pour retrouver les lettres associées aux chiffres puis retrouve le message.

    m = 0
    a = 0
    dico = {}
    for n in range (97,123) :
        dico[m] = chr(n)
        m+=1
    BonneForme = []
    TrucFinal = []
    for e in Code :
        Longueur = 0
        for i in str(e) :
            Longueur += 1
        if Longueur % 2 == 1 :
            BonneForme.append("0"+str(e))
        else :
            BonneForme.append(str(e))
    for e in BonneForme :
        compte = 1
        for b in e :
            a += int(b)*(10**compte)
            compte -= 1
            if compte == -1 :
                TrucFinal.append(dico[a])
                compte = 1
                a = 0
    return(TrucFinal)


p, q = GranbdNombresAleatoires() #Détermine les clés publiques
N = p*q
N2 = (p-1)*(q-1)
e = Grand(N2, N) #Détermine e en fonction de N et N2
k, d = CoeffDeBezout(N2, e) #Trouve les coeff de Bezout de N2 et eB

Message = str(input("Quelle message voulez vous codez? Seulement les lettres en minuscule et majuscules sans accents seront transcrites : "))
Decoupee = Decoupe(Message)
print(Decoupee)
Crypte = (Crypter(Decoupee, N, e))
print("Voici votre message crypté :", Crypte)
Decrypte = (Decrypter(Crypte, N, d))
print("Voici votre message décrypté :", Decrypte)
print("Votre message une fois retranscris donne :",Retrouve(Decrypte))