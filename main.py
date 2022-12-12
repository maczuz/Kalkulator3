def policz_suma(a, b):
    return a + b


def policz_roznica(a, b):
    return a - b


def policz_iloczyn(a, b):
    return a * b


def policz_iloraz(a, b):
    return a / b


def kalkulator(a, b, dzialanie):
    if dzialanie == "suma":
       return policz_suma(a, b)
    elif dzialanie == "roznica":
       return policz_roznica(a, b)
    elif dzialanie == "iloczyn":
       return policz_iloczyn(a, b)
    elif dzialanie == "iloraz":
        return policz_iloraz(a, b)
    else:
        print("bledne dzialanie")



def main():
    a = int(input())
    b = int(input())
    dzialanie = input()
    wynik = kalkulator(a, b, dzialanie)
    print(wynik)

    # a=int(input())
    # b =int(input())

if __name__ == '__main__':
    main()
