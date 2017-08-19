num=input("enter a number\n")
i=3
j=2
t=0
for i in range(2,num):
    for j in range(2,i):
        if(i%j==0):
            t=t+1
    if(t==0):
        print(i)
    t=0

#or

num=input("enter a number\n")
i=3
j=2
flag=0
for i in range(2,num):
    for j in range(2,i):
        if(i%j==0):
            flag=1
    if(flag<>1):
        print(i)
    flag=0
