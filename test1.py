arr=[]
n=input("ENter num")
a=0
b=1
i=0
c=0
arr.append(a)
arr.append(b)
while c<int(n):
    c=a+b
    a=b
    b=c
    print(c)
    arr.append(c)
    i=i+1
j=len(arr)
while j>0:
    print(arr[j-1]))
    j=j-1
