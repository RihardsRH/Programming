def krekli(skaits,apdruka,piegade):
    c = 0
    if apdruka == 1:#ja teik iedadīts "1" tad izvēlas teksta apdrukuy
        apdruka = 5#teksta apdrukas cena
        cena = apdruka*skaits#tiek aprēķināta cena ar noteikto kreklu daudzumu
    elif apdruka == 2:#ja  tiek ievadits "2" tad izvēlas zīmes apdruku
        apdruka = 7#zīmes apdrukas cena
        cena = apdruka*skaits#tiek aprēķināta cena ar noteikto kreklu daudzumu
    elif apdruka == 3:# ja tiek ievadīts "3" tad izvēlas ar foto apdruku
        apdruka = 20#foto apdurkas cena
        cena = apdruka*skaits#tiek aprēķināta cena ar noteikto kreklu daudzumu
    if piegade == 4 and cena <= 50:# ja izvēlēta piegāde ievada "4" un ja cena ir zem 50Eur tad cenai pieskaitīs 15Eur
        c = cena + 15#cenas aprēkāšana ar piegādes cenu
    if piegade == 5:# ja piegāde neizvēlēta tad ievada "5"
        c = c +cena#cena bez piegādes
    if c > 100:#ja cena pārsniedz 100Eur 
        ce = c*95/100#tiek aprēķināta 5% atlaide noteiktajai cenai
        print(ce)#izprintē gala cenu
    else:
        print(c)#izprintē gala cenu

#skaits = int(input("Ievadiet kreklu skaitu:"))
#apdruka = int(input("Ievadi apdrukas veidu (1-teksts I 2-zime I 3-foto):"))
#piegade = int(input("piegādi vajag(1) vai ne(2):"))
    

#krekli(skaits,apdruka,piegade)
krekli(10,3,5)#manuāli ievada attiecīgos definīcijas datus
