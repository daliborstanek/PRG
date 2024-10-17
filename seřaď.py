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
cisla.serad([25, 8, 17, 9, -1, 33, 16, 24, 5])
print(cisla)