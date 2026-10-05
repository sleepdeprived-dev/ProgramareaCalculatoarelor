# Problema 7: Cititi trei numere si verificati daca sunt in ordine crescatoare.

try:
    a = float(input("Scrie a: "))
    b = float(input("Scrie b: "))
    c = float(input("Scrie c: "))

    numere = [a, b, c]
    numere.sort()
    print(numere)

except ValueError:
    print("Trebuie sa scrii un numar.")