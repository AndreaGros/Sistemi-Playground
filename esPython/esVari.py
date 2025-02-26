# --- es 1 ---

def ribalta_Lista(lista):
    lista=lista[::-1]
    print(lista)
    return len(lista)

l=[1,2,3,4,5,6,7,8,9,10]
print(l)
ribalta_Lista(l)

# --- es 2 ---
def contaCifre(st):
    cont=0
    for ch in st:
        if(ch.isdigit()):
            cont+=1
    return cont

st=input()
print("Le cifre sono ", contaCifre(st))

# --- es 3 ---
def alternaListe(l, ls):
    r=[]
    for i in range(len(l)):
        r.append(l[i])
        r.append(ls[i])
    return r

l=[1,2,3,4,5,6,7,8,9,10]
ls=[11,12,13,14,15,16,17,18,19,20]
print(alternaListe(l, ls))

# --- es 4 ---
def contaAdiacenti(l):
    cont=0
    if(len(l)>1):    
        for i in range(1, len(l)):
            if(l[i]==l[i-1]):
                cont+=1
    return cont
        


l=[2,2,4,5,6,7,7,8,9,9]
print(l)
print(contaAdiacenti(l))

# --- es 5 ---
def bubble_sort(l):
    for n in range(len(l) - 1, 0, -1):
        swapped = False  
        for i in range(n):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                swapped = True
        if not swapped:
            break
l=[2,7,5,3,1,8,9,4]
print(l)
bubble_sort(l)
print(l)