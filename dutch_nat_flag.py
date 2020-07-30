n = int(input('enter the size of the list with only 0, 1, 2 '))
lst = list()
for i in range(n):
    ele = int(input('enter '))
    lst.append(ele)
print(lst)

def sort012(n, lst):
    low = 0
    mid = 0
    high = n-1
    #print(low,mid,high)
    while mid <= high :
        if lst[mid] == 0 :
            lst[low],lst[mid] = lst[mid],lst[low]
            low=low+1
            mid=mid+1
            #print('low',lst)
        elif lst[mid] == 1 :
            mid = mid + 1
            #print('mid',lst)
        else :
            lst[mid],lst[high] = lst[high],lst[mid]
            high=high-1
            #print('high',lst)
    return lst

lst = sort012(n, lst)
print('After sort ',lst)