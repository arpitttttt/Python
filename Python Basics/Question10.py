result_list = []
nr = int(input("Please enter a 4 digit number made from 0 and 1 : "))

if len(str(nr)) > 4:
    nr = int(input("Please enter a 4 digit number made from 0 and 1 : "))
elif str(nr).split():
    for x in str(nr):
        if x == 0 or x == 1:
            if nr % 5 == 0:
                result_list.append(nr)
            else:
                nr = int(input("Please enter a 4 digit number made from 0 "))
        else:
            nr = int(input("Please enter a 4 digit number made from 0 and 1 "))


else:
    print(result_list)