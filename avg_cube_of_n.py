n =  int(input('enter the number '))
sum = 0
cube = 0
for i in range(n+1) :
    cube = cube + (i**3)
print('The average of the number is', cube/n)