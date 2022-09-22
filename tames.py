#tāme ieklaujas :grīda(1.koka,2.linolejs,3.flizes)siena(1.regipsis,2.krasa,3.tapetes)logi(1.lielie,2.mazi),logu aizsegs(1.zalūzijas,2.aizskari), griezti(1.regipsis,2.krasa,3.plaksnu ornamenti)
a = float(input("ievadit kam vajadzigs aprekinat tames.(1 - grida I 2 - siena I 3 - griezti I 4 - G,S I 5 - G,Gr I 6 - "))#ja nav vajadzigs ievadīt 0
if a == 1 :
    g = float(input("Ievadiet gridas laukumu:"))
    gv = int(input("Ievadiet vēlamo materialu(1 koka, 2 linolejs, 3 flizes):"))
    if gv == 1:
        k = 5#koka summa uz 1 m^2
        gs = g*k


#elif a == 2:

#elif a == 3:#tests

#elif a == 4:

print(gs)