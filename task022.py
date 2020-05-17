string=str(input('enter the string'))
low_char=[]
upper_char=[]
for char in string:
    if char.islower():
        low_char.append(char)
    else:
        upper_char.append(char)
sortedstring=''.join(low_char+upper_char)
print(sortedstring)