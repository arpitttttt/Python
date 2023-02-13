side=int(input("Please enter any side of a square: "))
i=0
print("Square Star Pattern")
while(i < side):
    j=0
    while(j < side):
        j=j+1
        print('*',end='')
    i=i+1
    print()


