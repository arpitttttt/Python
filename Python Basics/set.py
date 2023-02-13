text=input("Enter the text\n")

if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("subscribe now" in text):
    spam=True
else:
    spam=False
    
if(spam):
    print("This is spam")
else:
    print("this text is not a spam")