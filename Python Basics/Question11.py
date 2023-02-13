s=input("Enter your Statement:")

#def findLetterandDigits(s):

letter_count=0
digit_count=0

for count in s:
    if count.isdigit():
            digit_count+=1
    elif count.isalpha():
            letter_count+=1

    #return letter_count,digit_count

    #letters,digits = findLetterandDigits(s)

    print("No. of letter:",letter_count)
    print("No. of digits:",digit_count)