from math import sqrt


def generaLista(n):
    lst = []
    for x in range(1, n + 1):
        lst.append(x)
    return lst


def multipli(nInput, nMax):
    multipli = []
    i = 2
    while nInput * i <= nMax:
        multipli.append(nInput * i)
        i += 1
    return multipli


print("Inserisci un numero:", end=" ")
numero = int(input())
lstNumeri = generaLista(numero)


for x in range(2, int(sqrt(numero)) + 1):
    lstMulti = multipli(x, numero)
    for digit in lstMulti:
        if digit in lstNumeri:
            lstNumeri.remove(digit)
print(lstNumeri)
