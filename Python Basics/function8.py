def remove_and_strip(string,word):
    newStr=string.replace(word,"")
    return newStr.strip()
this="Hello WoRLD"
a=remove_and_strip(this,"Hello")
print(a)