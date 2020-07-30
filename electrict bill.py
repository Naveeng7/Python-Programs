units =  int(input('enter the units consumed '))

if units <= 100 :
    bill = 10*units
elif units <= 200 :
    bill = (10*100) + ((units-100)*15)
elif units <= 300 :
    bill = (10*100) + (15*100) + (20*(300-units))
else :
    bill = (10*100) + (15*100) + (20*100) + (25*(units-300))

print('the bill is', bill)