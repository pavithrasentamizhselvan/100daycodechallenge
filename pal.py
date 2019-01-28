str=['r','*','d','a','r']
i=0
print(str)
length=len(str)
print(str[1])
print(str[length-1])
print(str[i]==str[length-1])
while i<length:
    if(str[i]==str[length-i-1]):
        pass
    else:
        str[i]=str[length-i-1]
    i=i+1
print(str)
