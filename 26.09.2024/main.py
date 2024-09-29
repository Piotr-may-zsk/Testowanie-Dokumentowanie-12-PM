#**********************************************
#   nazwa funkcji: sprawdzPlec
#   opis funkcji: odczytuje plec z danego peselu
#   parametry: pesel - tablica znakow
#   zwracany typ i opis: str - zwraca K (jezeli kobieta) lub M (jezeli mezczyzna)
#   autor: Piotr May
#***********************************************

def sprawdzPlec(pesel):
    if(int(pesel[9]) % 2 == 0):
        return 'K'
    return 'M'

#**********************************************
#   nazwa funkcji: sprawdzSume
#   opis funkcji: sprawdza sume kontrolna peselu
#   parametry: pesel - tablica znakow
#   zwracany typ i opis: boolean - czy suma jest poprawna
#   autor: Piotr May
#***********************************************

def sprawdzSume(pesel):
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    S=0
    znak=0
    for i in pesel:
        if(znak < 10):
            S+=(int(i) * wagi[znak])
            znak+=1

    M=S%10

    if(M==0):
        R = 0
    else:
        R = 10-M

    return R == int(pesel[10])


pesel = input("Podaj pesel: ")
if pesel is None or len(pesel) < 11:
    pesel = "55030101193"

if (sprawdzPlec(pesel) == 'K'):
    print("Kobieta")
elif(sprawdzPlec(pesel) == 'M'):
    print("Mezczyzna")


if(sprawdzSume(pesel)):
    print("PESEL poprawny")
else:
    print("PESEL niepoprawny")
