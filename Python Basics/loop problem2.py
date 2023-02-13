list=[]
while True:
    x=int(input("Number"))
    if x>0:
        list.append(x)
        if x<0:
            print(sum(list))
            break
