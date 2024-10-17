class Parabola:
    
    def __init__(self, a, b, c):
        self.a = a if (a != 0) else 1
        self.b = b
        self.c = c
        self.determinant = self.get_determinant()
        
    def get_determinant(self):
        return self.b ** 2 - 4 * self.a * self.c

p = Parabola(5, 3, 7)
print(p.a)
print(p.get_determinant())