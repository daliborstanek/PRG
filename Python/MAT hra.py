from random import randint

def start_game():
    print("\nVítej v procvičování matematiky.")
    print("Můžeš zde procvičovat sčítání, odčítání a násobení.")
    print("Co by jsi chtěl zkusit?")
    print("A - sčítání")
    print("B - odčítání")
    print("C - násobení")
    print("D - Ukončit Hru\n")
    
    choice = input()
    
    if choice == "A":
        addition()
    elif choice == "B":
        subtraction()
    elif choice == "C":
        multiplication()
    elif choice == "D":
        return None
    else:
        print("To není v nabídce, zkus to znovu.\n")
        start_game()

def addition():
    num_1 = randint(0,9)
    num_2 = randint(0,9)
    
    print(f"Kolik je {num_1} + {num_2} ?\n")
    
    choice = input("> ")
    
    if int(choice) == num_1 + num_2:
        print("Správně! Hraj dál!\n")
        start_game()
    else:
        print(f"Špatně, výsledek je {num_1 + num_2}!\n")
        start_game()
        
def subtraction():
    num_1 = randint(0,9)
    num_2 = randint(0,9)
    
    print(f"Kolik je {num_1} - {num_2} ?\n")
    
    choice = input("> ")
    
    if int(choice) == num_1 - num_2:
        print("Správně! Hraj dál!\n")
        start_game()
    else:
        print(f"Špatně, výsledek je {num_1 - num_2}!\n")
        start_game()

def multiplication():
    num_1 = randint(0,9)
    num_2 = randint(0,9)
    
    print(f"Kolik je {num_1} x {num_2} ?\n")
    
    choice = input("> ")
    
    if int(choice) == num_1 * num_2:
        print("Správně! Hraj dál!\n")
        start_game()
    else:
        print(f"Špatně, výsledek je {num_1 * num_2}!\n")
        start_game()
        
start_game()
