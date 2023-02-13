def remove_and_split(string,word):
    newStr=string.replace(word,"")
    return newStr.strip()

this="  Arpit is a good boy  "
n=remove_and_split(this,"good")
print(n)