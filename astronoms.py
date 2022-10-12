import random
horoskopi = ["Auns", "Vērsis", "Dvīņi", "Vēzis", "Lauva", "Jaunava", "Svari", "Skorpions", "Strēlnieks", "Mežāzis", "Ūdensvīrs", "Zivis"]
a1 = ["Centieties visu novērtēt lietišķi,nepakļaujieties emocijām","Svārstīsieties vai uzstādīt stingrākas prasības līdzcilvēkiem.",
"Šodien lieli panākumi nav gaidāmi,bet varat izvairīties no zaudējuma.",
"Kādu ideju vēlēsieties īstenot bez kavēšanās, tomēr ieteicas neteigies.","Uzņemieties iniciatīvu kāda darbaveikšanai.",
"Nebūsiet gatavs kompromisiem, tasapgrūtinās lēmumu pieņemšanu.","Ļaujiet notikumiem notikt dabiski,nesteidziniet tos.","Varat iegūt jaunus sadarbības partnerus.",
"Nepieļaujiet vieglprātību nevienā jomā.","Savus nodomus pārvērtējiet vēl un vēlreiz.",
"Neļaujieties īgnumam. ","Gādājiet par mājas miera uzturēšanu."]
a2 = ["Par palīgiem izvēlieties cilvēkus, kuri ir jums uzticami.","Esiet izlēmīgs, bet ne sīkumains.",
"Apmeklējiet vecākus radiniekus.","Nepieprasiet no iemīļotās personas, lai viņa apmierina visas jūsu vēlmes.",
"Neuztveriet jebkuru apgalvojumu par augstāko patiesību, spriediet un salīdziniet pats.","Nav ieteicams šodien mainīt darbu.",
"Kādu jaunu ziņu nepratīsiet pozitīvi novērtēt.","Sniedziet palīdzību tiem, kam tā nepieciešama un negaidiet pateicību.",
"Lietišķās sarunās nepieciešama noteiktība, nepaļaujieties uz miglainiem solījumiem.","Nepaļaujieties uz solījumiem, bet varat sadarboties ar draugiem.",
"Negaidiet, lai partneris risinātu jūsu problēmas.","Pārrunājiet lietas ar iemīļoto personu."]
a3 = ["ap31","ap32","ap33","ap34","ap35","ap36","ap37","ap38","ap39","ap310","ap311","ap312"]
r1 = ["ri1","ri2","ri3","ri4","ri5","ri6","ri7","ri8","ri9","ri10","ri11","ri12"]
for i in range(len(horoskopi)):#iziet cauri katram horoskopam
    print("Jūsu horoskops",horoskopi[i],"šodien prognozē.","\n")#parāda horoskopu
    aa1 = random.choice(a1)#nejauši izvēlās vienu teikumu no a1 lista
    print(aa1)
    a1.remove(aa1)
    aa2 = random.choice(a2)
    print(aa2)
    a2.remove(aa2)
    aa3 = random.choice(a3)
    print(aa3)
    a3.remove(aa3)
    rr1 = random.choice(r1,)
    print(rr1,"\n")
    r1.remove(rr1)



