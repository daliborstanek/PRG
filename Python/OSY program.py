import random
A = ["polévka", "vývar", "krém", "kaldoun"]
B = ["hovězí", "kuřecí", "kachní", "gulášová", "frankfurtská", "hrachová", "květáková", "brokolicová"]
C = ["s rýží", "s celestýnskými nudlemi", "s baby karotkou", "s krutony", "se zavářkou", "s nudlemi"]

for i in range(5):
    print (random.choice(B) + " " + random.choice(A) + " " + random.choice(C))
