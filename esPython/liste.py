l1=[2, 3, 5, 6, 7, 9]
l2=[1, 4, 5, 8, 10, 15, 22]
l3=[]
i=0
j=0
while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
        l3.append(l1[i])
        i += 1
    elif l1[i] > l2[j]:
        l3.append(l2[j])
        j += 1
    else:
        l3.append(l1[i])
        l3.append(l2[j])
        i += 1
        j += 1

while i < len(l1):
    l3.append(l1[i])
    i += 1

while j < len(l2):
    l3.append(l2[j])
    j += 1

print(l3)