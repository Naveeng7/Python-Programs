def clst(n):
    lst = list()
    for i in range(n):
        ele = int(input('Enter '))
        lst.append(ele)
    return lst

m = int(input('Enter the size '))
lst1 = clst(m)

n = int(input('Enter the size '))
lst2 = clst(n)

print(lst1,'\n',lst2)


def merge(arr1, arr2, x, y):

    for i in range(y-1, -1, -1):
        last = arr1[x-1]
        pos = x-2
        while pos >= 0 and arr1[pos] > arr2[i] :
            arr1[pos+1] = arr1[pos]
            pos-=1

        if pos != m-2 or last > arr2[i]:
            arr1[pos+1] = arr2[i]
            arr2[i] = last

def pri(s, lt):
    for i in range(s):
        print(lt[i],end=' ')

merge(lst1, lst2, m, n)

pri(m, lst1)
print()
pri(n, lst2)
