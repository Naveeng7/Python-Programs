def lstc(n):
    lst = list()
    for i in range(n):
        ele = int(input('enter '))
        lst.append(ele)
    return lst

def lapp(ele, lst):
    lst.append(ele)
    return lst

m = int(input('enter the size of the 1st list '))
lst1 = lstc(m)
n = int(input('enter the size of the 2nd list '))
lst2 = lstc(n)

print('The list are \n',lst1, '\n',lst2)

#sort
lst3 = list()
i = 0
j = 0
k= m + n -1
while i < m and j < n :
    if lst1[i] < lst2[j] :
        lst3 = lapp(lst1[i], lst3)
        i = i + 1
    else:
        lst3 = lapp(lst2[j],lst3)
        j = j + 1

x=i
y=j

while i < m or j < n:
    if i < m :
        for i in range(x, m):
            #print('i',i)
            lst3  = lapp(lst1[i],lst3)
            i = i + 1
    if j < n :
        for j in range(y, n) :
            #print('j',j)
            lst3 = lapp(lst2[j],lst3)
            j = j+ 1

print('The sorted list is :',lst3)