


num=int(input("Enter the fucking number"))
prime=True

for i in range(2,num):
    if(num%i==0):
        prime=False
        break
    if prime:
        print("This is a prime Number")
    else:
        print("This not a prime number")

