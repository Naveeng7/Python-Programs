lst = list()
n = int(input('enter the size of the list '))
for i in range(n) :
    ele = int(input('enter '))
    lst.append(ele)
print('The list is ',lst)

dct = dict()

for i in range(n):
    dct[lst[i]] = dct.get(lst[i], 0) + 1
print(dct)

print('The duplicate elements are :')
for i in dct :
    if  dct[i] > 1 :
        print(i,end=' ')