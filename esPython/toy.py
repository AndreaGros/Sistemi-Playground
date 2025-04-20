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

print(ese1(a, b))
print(ese2(42165))
print(ese3(5, -1))
a = [5, 3, 2, 4, 1, 8]
print(ese4(a))
print(cesare("abc"))
