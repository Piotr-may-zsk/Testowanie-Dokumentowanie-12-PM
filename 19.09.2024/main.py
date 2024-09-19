import random


#************************************************
#nazwa: rzuc_kostkami
#opis: Funkacja losuje wynik rzutu dla każdej z kości
#parametry: liczba_kostek - liczba całowita kostek do rzutu
#zwracany typ i opis: tablica liczb całkowitych
#autor: Piotr May
#************************************************

def rzuc_kostkami(liczba_kostek):
    wyniki = []
    for i in range(liczba_kostek):
        wynik_rzutu = random.randint(1, 6)
        wyniki.append(wynik_rzutu)
    return wyniki


#************************************************
#nazwa: wypisz_wyniki
#opis: Funkacja wypisuje wynik rzutu dla każdej z kości
#parametry: wyniki - tablica wyników rzutów kostek
#zwracany typ i opis: brak
#autor: Piotr May
#************************************************
def wypisz_wyniki(wyniki):
    for i in range(len(wyniki)):
        print(f'Kostka {i}: {wyniki[i]}')


#************************************************
#nazwa: policz_punkty
#opis: Liczy punkty uzyskane z rzuty kośćmi
#parametry: wyniki_rzutow - tablica wyników rzutów kostek
#zwracany typ i opis: liczba całkowita - punkty uzyskane za rzuty
#autor: Piotr May
#************************************************
def policz_punkty(wyniki_rzutow):
    wyniki_rzutow = sorted(wyniki_rzutow)
    suma_punktow = 0
    liczba_kostek = len(wyniki_rzutow)
    for i in range(liczba_kostek - 1):
        if wyniki_rzutow[i] == wyniki_rzutow[i + 1] or wyniki_rzutow[i] == wyniki_rzutow[i - 1]:
            suma_punktow += wyniki_rzutow[i]

    if wyniki_rzutow[liczba_kostek - 1] == wyniki_rzutow[liczba_kostek - 2]:
        suma_punktow += wyniki_rzutow[liczba_kostek - 1]
    return suma_punktow


if __name__ == '__main__':
    print("Ile kostek chcesz rzucić?(3 - 10)")
    liczba_kostek = int(input())
    if liczba_kostek < 1:
        print("Błędnie podana liczba kostek")
    else:
        czy_jeszcze_raz = True
        while czy_jeszcze_raz:
            wyniki_rzutow = rzuc_kostkami(liczba_kostek)
            wypisz_wyniki(wyniki_rzutow)
            suma_punktow = policz_punkty(wyniki_rzutow)
            print(f'Liczba uzyskanych punktow: {suma_punktow}')
            print("Jeszcze raz?")
            decyzja = input()
            czy_jeszcze_raz = decyzja == "t"