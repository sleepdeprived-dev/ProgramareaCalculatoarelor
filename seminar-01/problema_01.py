# Problema 1: Cititi un numar n si afisati dublul sau.

try:
    n = float(input("Introdu un numar: "))
    print(f"{n} * 2 = {n * 2}")
except ValueError:
    print("Trebuie sa fie un numar.")