def is_leap(year):
    leap = False
    
if (year % 400 == 0) and (year % 100 == 0):
        
    leap = True

elif (year % 4 ==0) and (year % 100 != 0):
        
        leap = True
else:


return leap


year = int(input())
print(is_leap(year))