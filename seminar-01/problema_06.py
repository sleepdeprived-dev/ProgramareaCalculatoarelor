# Problema 6: Cititi trei numere si determinati valoarea maxima.

try:
    a = float(input("Scrie a: "))
    b = float(input("Scrie b: "))
    c = float(input("Scrie c: "))

    if a > b and a > c:
        print(f"{a} este cel mai mare.")
    elif b > a and b > c:
        print(f"{b} este cel mai mare.")
    elif c > a and c > b:
        print(f"{c} este cel mai mare.")
    elif a == b == c:
        print("Cele 3 sunt egale.")

except ValueError:
    print("Ar trebui sa scrii un numar.")