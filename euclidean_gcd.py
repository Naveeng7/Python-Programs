def hcf(m,n):
    if m == 0:
        return n
    return hcf(n%m, m)

x = int(input('Enter the 1st value '))
y = int(input('Enter the 2nd value '))
ans = hcf(x,y)

print('The HCF of',x,'and',y,'is',ans)