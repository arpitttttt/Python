def print_Table_Number(num):
    for i in range(1,11):
        print(num,'x',i,'=',num*i)
n=int(input("Enter a number for its table: "))
print_Table_Number(n)