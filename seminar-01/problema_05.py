# Problema 5: Cititi trei numere si calculati suma si media lor

try:
    a = float(input("Scrie primul numar: "))
    b = float(input("Scrie al doilea numar: "))
    c = float(input("Scrie al treilea numar: "))
    medie = (a + b + c) / 2

    print(f"{a} + {b} + {c} = {a+b+c}")
    print(f"Media dintre {a}, {b} si {c} este {medie}.")

except ValueError:
    print("Ar trebui sa scrii un numar.")
