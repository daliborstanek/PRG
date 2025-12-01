from random import randint

def start_game():
    print("\nToto je hra o hádání číslic.")
    print("A - začít hrát")
    print("B - ukončit hru")
    
    choice = str(input())
    
    if choice == "A" or "a":
        guess()
    elif choice == "B" or "b":
        return None
    else:
        print("To není v nabídce, zkus to znovu.")
        
def guess():
    print("Zkus uhádnout správné číslo od 1 do 2")
    
    num = randint(0,2)
    user_guess = int(input())
    
    if user_guess == num:
        print("Výborně, uhádl jsi číslo!")
    else:
        print("Špatně, nevadí, zkus to znovu.")
        
start_game()
