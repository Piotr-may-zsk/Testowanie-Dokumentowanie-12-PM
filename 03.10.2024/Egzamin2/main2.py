
# *********************************************
# nazwa funkcji: NWD
# opis funkcji: Funkcja oblicza NWD
# parametry: a - liczba naturalna dodatnia
#  nazwa parametru b - liczba naturalna dodatnia
# zwracany typ i opis: liczba naturalna dodatnia - NWD
# autor: Piotr May
# ***********************************************
def NWD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def main():
    print('Wprowadz a i b:')
    a = int(input("a: "))
    b = int(input("b: "))
    if a > 0 and b > 0:
        wynik = NWD(a, b)
        print('NWD to: ', wynik)
    else:
        print("Wprowadz poprawne dane!")


main()
