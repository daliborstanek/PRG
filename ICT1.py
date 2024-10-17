import math

# První úkol
print("Zadej rychlost m/s")
ms = int(input())

kmh = ms * 3.6
print(int(kmh), "km/h")

# Druhý úkol
print("Zadej teplotu v 6 hodin")
hodina_06 = int(input())
print("Zadej teplotu v 12 hodin")
hodina_12 = int(input())
print("Zadej teplotu v 18 hodin")
hodina_18 = int(input())

průměr = (hodina_06 + hodina_12 + hodina_18 + hodina_18) / 4
print(průměr, "°C")

# Třetí úkol
print("Zadej délku strany A")
a = int(input())
print("Zadej délku strany B")
b = int(input())
math.sqrt(a)
math.sqrt(b)

c = a ** 2 + b ** 2
print("Délka přepony je", int(math.sqrt(c)))

# Čtvrtý úkol
print("Zadej číslo plánovaných produktů")
plánované = int(input())
print("Zadej číslo vyrobených produktů")
vyrobeno = int(input())

splněno = vyrobeno / plánované * 100
print(int(splněno), "% produktů")

# Pátý úkol
print("Zadej hodnotu X")
x = int(input())
print("Zadej hodnotu Y")
y = int(input())

if y * x + 3 < 5 * y - 1:
    print("Ano")
else:
    print("Ne")
    
# Šestý úkol
print("Zadej rozměr A")
a = int(input())
print("Zadej rozměr B")
b = int(input())

if a == b:
    print("Čtverec má rozměry", a, "cm", "x", b, "cm")
else:
    print("Obdelník má rozměry", a, "cm", "x", b, "cm")
    
# Sedmý úkol
čísla = [-6, 4, -12]

čísla.sort(reverse = True)
print(*čísla, sep = ", ")