import math

# ******************************************************
#  nazwa funkcji: znajdzLiczbyPierwsze
#  parametry wejściowe: Tablica boolean - wypełniona wartościami True
#  wartość zwracana: brak
#  informacje: Funkcja wyszukuje liczby pierwsze mniejsze od 100
#  autor: Piotr May
# ****************************************************
def znajdzLiczbyPierwsze(A):
    for i in range(2, int(math.sqrt(n))):
        if A[i]==True:
            for j in range(2*i,n,i):
                A[j]=False

    print('Liczby pierwsze: ')
    for i in range(2, len(A)):
        if A[i]==True:
            print(i,end=" ")


n=100
A=[]
for i in range(n):
    A.append(True)

znajdzLiczbyPierwsze(A)