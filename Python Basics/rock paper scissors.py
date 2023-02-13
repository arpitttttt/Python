import random

user_input = input("Enter your choice: Rock Scissors Paper ")
available_choices=["Rock" , "Scissors" , "Paper"]
comp = random.choice(available_choices)
print(f"Your choices{user_input} , Comp{comp}")

if user_input==comp:
    print("You both have chosen same, This is a tie")
elif user_input=="Rock":
    if comp == "Scissors":
        print("Comp Lost")
    else:
        print("You Win")
elif user_input=="Paper":
    if comp=="Rock":
        print("AHH!, You Win ")
    else:
        print("Loose")
elif user_input=="Scissors":
    if comp=="Paper":
        print("You win as u're smart enough for this")
    else:
        print("You Loose bitch")


