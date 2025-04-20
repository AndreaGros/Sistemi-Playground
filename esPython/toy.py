import re

a = [1, 2, 2, 2, 3, 5, 6, 8, 9]
b = [2, 8]


def ese1(a, b):
    for x in a:
        if x in b:
            a.remove(x)
    return a


def ese2(n):
    m = str(n)
    y = int("".join(sorted(m, reverse=True)))
    return y


def ese3(a, b):
    n = 0
    if a > b:
        a, b = b, a
    for x in range(a, b + 1):
        n += x
    return n


def ese4(a):
    c = []
    for x in a:
        if x % 2 == 0:
            c.append(x)
    c.sort()
    i = 0
    j = 0
    for x in a:
        if x in c:
            a[i] = c[j]
            j += 1
        i += 1
    return a


def cesare(string):
    encrypted = ""
    for c in string:
        if "a" <= c <= "z":
            charEncrypted = chr((ord(c) - ord("a") + 13) % 26 + ord("a"))
        elif "A" <= c <= "Z":
            charEncrypted = chr((ord(c) - ord("A") + 13) % 26 + ord("A"))
        else:
            charEncrypted = c
        encrypted += charEncrypted
    return encrypted


def validateIP(IP):
    numeri = IP.split(".")
    if len(numeri) == 4:
        for numero in numeri:
            if numero.startswith("0") or int(numero) not in range(255 + 1):
                break
        else:
            return "Indirizzo valido"
    return "Indirizzo non valido"


def differenzaIP(IP1, IP2):
    IP1 = IP1.split(".")
    IP2 = IP2.split(".")
    print(IP1, IP2)

    i = 3
    diff = 0
    for byte1, byte2 in zip(IP1, IP2):
        diff += (int(byte2) - int(byte1)) * pow(256, i)
        i -= 1
    return diff


def ISBM(ISBM):
    somma = 0
    for cifra, i in zip(ISBM, range(1, len(ISBM) + 1)):
        if cifra.isdigit():
            somma += int(cifra) * i
        else:
            somma += 10 * i
    if somma % 11 == 0:
        return True
    return False

def ese9(a, b):
    l=[]
    for i in range(a, b+1):
        if(i%7==0 and not i%5==0):
            l.append(str(i))
    return ",".join(l)
        
    


print(ese1(a, b))
print(ese2(42165))
print(ese3(5, -1))
a = [5, 3, 2, 4, 1, 8]
print(ese4(a))
print(cesare("abc"))
print(validateIP("192.168.15.255"))
print(differenzaIP("192.0.0.0", "192.1.1.0"))
print(ISBM("048665088X"))
print(ese9(100, 200))
