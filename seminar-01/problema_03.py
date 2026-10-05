# Problema 3: Cititi doua numere si determinati valoarea maxima

try:
    a = float(input("Introdu un numar: "))
    b = float(input("Introdu un alt numar: "))
    if a > b:
        print(f"{a} > {b}")
    elif a == b:
        print(f"{a} == {b}")
    else:
        print(f"{b} < {a}")
except ValueError:
    print("Trebuie sa fie un numar.")