# Problema 4: Cititi doua numere si sa se afiseze in ordine crescatoare.

try:
    a = float(input("Introdu primul numar: "))
    b = float(input("Introdu al doilea numar: "))
    if a > b:
        print(f"{b}, {a}")
    else:
        print(f"{a}, {b}")
except ValueError:
    print("Trebuie sa scrii un numar.")