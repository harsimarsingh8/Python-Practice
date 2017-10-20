sum=0
n=input("enter the number of digits\n")
num=input("enter the number\n")
old=num 
while(num!=0):
    num1=num%10 
    sum=sum+(num1**n)
    num=num/10
if(old==sum): 
    print("armstrong")
else: 
     print("not armstrong")
    
