#def krekli(skaits,apdruka,piegade):

skaits = int(input("Ievadiet kreklu skaitu:"))
apdruka = int(input("Ievadi apdrukas veidu (1-teksts I 2-zime I 3-foto):"))
piegade = input("piegādi vajag(1) vai ne(2):")
if apdruka == 1:
    apdruka = 5
    cena = apdruka*skaits
elif apdruka == 2:
    apdruka = 7
    cena = apdruka*skaits
elif apdruka == 3:
    apdruka = 20
    cena = apdruka*skaits
if piegade == True and cena <= 50:
    cena =cena + 15
print(cena)
if piegade == False:
    print(cena)
    
    










#krekli(skaits,apdruka,piegade)

