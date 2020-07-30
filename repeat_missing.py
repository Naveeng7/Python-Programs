n = int(input('enter the list size '))
lst = list()
for i in range(n) :
    ele = int(input('enter '))
    lst.append(ele)
print(lst)

#for repeated element
repeated = 0
for i in range(0, n+1):
    if i not in lst and i != 0 :
        print('Missing number is:',i)
    for j in range(i+1, n):
        #print(i,j,lst[i],lst[j])
        if lst[i] == lst[j] :
            repeated = lst[i]


print('repeated number is:',repeated)
