def calc():
    print("Vyber si operaci")
    print("A - sčítání")
    print("B - odčítání")
    print("C - násobení")
    print("D - dělení")
    print("E - ukončit program")
    
    operace = input("Zadej písmeno operace: ")
    
    if operace == "A" or "a":
        num1 = float(input("Zadej první číslo: "))
        num2 = float(input("Zadej druhé číslo: "))
        výsledek = num1 + num2
        print(výsledek)
        
    elif operace == "B" or "b":
        num1 = float(input("Zadej první číslo: "))
        num2 = float(input("Zadej druhé číslo: "))
        výsledek = num1 - num2
        print(výsledek)
        
    elif operace == "C" or "c":
        num1 = float(input("Zadej první číslo: "))
        num2 = float(input("Zadej druhé číslo: "))
        výsledek = num1 * num2
        print(výsledek)
        
    elif operace == "D" or "d":
        num1 = float(input("Zadej první číslo: "))
        num2 = float(input("Zadej druhé číslo: "))
        if num2 == 0:
            print("Nelze delit nulou.")
        else:
            výsledek = num1 / num2
            print(výsledek)
        
    elif operace == "E" or "e":
        return None
        
calc()