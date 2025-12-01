import math

class Kruznice:

    def __init__(self, d):
       self.d = d

    def má_obvod(self):
        return self.d * math.pi

    def má_obsah(self):
        r = self.d / 2
        return math.pi * r**2

    def __str__(self):
        obvod = self.má_obvod()
        obsah = self.má_obsah()
        return "Kružnice o průměru {self.d} má obvod {obvod:.2f} a obsah {obsah:.2f}."

d = str(input("Zadej průměr kružnice"))
k = Kruznice(d)
print(k)
