import random
l=[1,2,3,4,5]*2
random.shuffle(l)
for i in range(len(l)):
    print("x ", end="")
print("\n")
cont=0
while(cont!=len(l)/2):
    pos=int(input())
    for i in range(len(l)):
        if(i==pos):
            print(l[pos]," ", end="")
        else:
            print("x ", end="")
    pos2=int(input())
    if(l[pos]==l[pos2]):
        cont+=1

