# Seřadí čísla sestupně nebo vzestupně
class Sorting:
  
  def __init__(self):
    self.cisla = []
    self.smer = "vzestupne" 
    
  def serad(self, seznam_cisel, smer = "vzestupne"):
    self.cisla = seznam_cisel
    if (smer == "vzestupne"):
      self.cisla.sort()
    elif (smer == "sestupne"):
      self.cisla.sort(reverse = True)
      
  def __str__(self):
    return str(self.cisla)

cisla = Sorting()
cisla.serad([25, 8, 17, 9, -1, 33, 16, 24, 5], "vzestupne")
print(cisla)

prvocisla = Sorting()
prvocisla.serad([13, 5, 17, 23, 2, 3, 7, 11], "vzestupne")
print(prvocisla)

cisla2 = Sorting()
cisla2.serad([3.14, 2.91, -57, 64.8, 2.7818281828, 0x25, 0o17, 0b11010110111, 3e-1], "vzestupne")
print(cisla2)