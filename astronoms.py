import random
horoskopi = ["Auns", "Vērsis", "Dvīņi", "Vēzis", "Lauva", "Jaunava", "Svari", "Skorpions", "Strēlnieks", "Mežāzis", "Ūdensvīrs", "Zivis"]
a1 = ["ap11","ap12","ap13","ap14","ap15","ap16","ap17","ap18","ap19","ap120","ap121","ap122"]
a2 = ["ap21","ap22","ap23","ap24","ap25","ap26","ap27","ap28","ap29","ap230","ap231","ap232"]
a3 = ["ap31","ap32","ap33","ap34","ap35","ap36","ap37","ap38","ap39","ap310","ap311","ap312"]
r1 = ["ri1","ri2","ri3","ri4","ri5","ri6","ri7","ri8","ri9","ri10","ri11","ri12"]
for i in range(len(horoskopi)):
    print(horoskopi[i],"\n")
    aa1 = random.choice(a1)
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



