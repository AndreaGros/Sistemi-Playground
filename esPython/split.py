def merge(left, right):
    l = r = 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    if l < len(left):
        result.extend(left[l:])
    else:
        result.extend(right[r:])

    return result


def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    left = lista[: len(lista) // 2]
    right = lista[len(lista) // 2 :]
    print(left, right)
    left = merge_sort(left)
    right = merge_sort(right)
    print(left, right)
    return merge(left, right)


lista1 = [2, 3, 5, 6, 7, 9]
lista2 = [1, 4, 5, 8, 10, 15, 22]
lista = lista1 + lista2 + lista1 + [7, 99, 3]
print("La prima losta ordinata è : ", lista1)
print("La seconda lista ordina è:", lista2)
print(merge_sort(lista))
