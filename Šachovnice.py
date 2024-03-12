velikost = 8

sachovnice = [[(i + j) % 2 for j in range(velikost)] for i in range(velikost)]

for radek in sachovnice:
    print(radek)