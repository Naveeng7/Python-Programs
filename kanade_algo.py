m = int(input('Enter the size '))
lst1 = list()
for i in range(m):
    ele  = int(input('Enter '))
    lst1.append(ele)

print(lst1)

maxval = -999
maxend = 0

for i in range(0, m):
    maxend = maxend + lst1[i]

    if maxval < maxend :
        maxval = maxend

    if maxend < 0:
        maxend = 0

print(maxval)