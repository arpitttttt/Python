#def print_table(n, i=1):
 
   # if (i == 11):  # base case
       # return
    #print(n, "*", i, "=", n * i)
    #i += 1  # increment i
   ## print_table(n, i)
 
# Driver Code
#n = int(input("Enter your number:"))
#print_table(n)
# Printing the Multiplication table in Python - Using for loop

num = int(input ("Please enter the number for which we want to print the multiplication table of: "))

print( 'Lets print the table of:' , (num))

# Used print statement to validate the num variable and the user input

# For hardcoding the code , use num = n, where n is the number for which we want to print the multiplication table.

# Using for loop, we  are iterating up to 10 times that is, from s = 1 to s =10

for i in range(1, 11):
    print(num, 'x', i, '=', num*i)
    
