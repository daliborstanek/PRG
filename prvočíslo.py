def je_prvočíslo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Zadej číslo: "))
if je_prvočíslo(num):
    print(f"Číslo {num} je prvočíslo.")
else:
    print(f"Číslo {num} není prvočíslo.")