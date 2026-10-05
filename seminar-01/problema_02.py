# Problema 2: Cititi doua numere a si b si afisati suma, diferenta, produsul si media

try:
    a = float(input("Scrie primul numar: "))
    b = float(input("Scrie al doilea numar: "))
    medie = (a+b) * 0.5
    print(f"{a} + {b} = {a+b}")
    print(f"{a} - {b} = {a-b}")
    print(f"{a} * {b} = {a*b}")
    print(f"Media dintre {a} si {b} este {medie}")
except ValueError:
    print("Trebuie sa fie un numar.")

