velikost = 8

šachovnice = [[(i + j) % 2 for j in range(velikost)] for i in range(velikost)]

for řádek in šachovnice:
    print(řádek)
