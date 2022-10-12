def krekli(skaits,apdruka,piegade):
    c = 0
    if apdruka == 1:
        apdruka = 5
        cena = apdruka*skaits
    elif apdruka == 2:
        apdruka = 7
        cena = apdruka*skaits
    elif apdruka == 3:
        apdruka = 20
        cena = apdruka*skaits
    if piegade == 4 and cena <= 50:
        c = cena + 15
    if piegade == 5:
        c = c +cena
    if c > 100:
        ce = c*95/100
        print(ce)
    else:
        print(c)

#skaits = int(input("Ievadiet kreklu skaitu:"))
#apdruka = int(input("Ievadi apdrukas veidu (1-teksts I 2-zime I 3-foto):"))
#piegade = int(input("piegādi vajag(1) vai ne(2):"))
    

#krekli(skaits,apdruka,piegade)
krekli(10,3,5)#manuāli ievada attiecīgos definīcijas datus
