i=1
while True:
    print(i)
    break
i+=1
print("ciao")

#list comprehension
lista=[x for x in range(1,11) if x%2 ==0]
print(lista)

senza_vocali=[c for c in "salve mondo" if c not in "aeiou"]
print(senza_vocali)
str="".join(senza_vocali)
print(str)

a=1
b=a
a=2
print(a, b)

q3_lst = ['peanut', 'butter', '&','jelly']
print(q3_lst[-3:])

ex2_lst = [0, False, 'ten', None]

bool_1 = False in ex2_lst
bool_2 = 10 not in ex2_lst

output = bool_1 and bool_2

print(output)

a = (1,)
b = a
a = (2,)

a = [1]
b = a
a[0] = 2

print(a,b)

counter = 0
my_lst = [False, True, False, True]

for item in my_lst:
    if item:
        continue
    else:
        counter = counter + 1

print(counter)


number = 1

while True:
    if number % 3 == 0:
        break

    print(number)

    number = number + 1

    def exponentiate(number, exponent=2):
        function_output = number ** exponent
        return function_output

print(exponentiate(exponent=3, number=2))
