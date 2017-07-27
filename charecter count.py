#to count the characters in a string
##x=raw_input("enter string\n")
##temp=set(x)
##temp1=list(temp)
##for i in temp1:
##    print i
##    n=x.count(i)
##    print n
##    

s=raw_input("enter string\n")
count=1
n=len(s)
temp=" "
for i in range(0,n-1,1):
        if(s[i]==s[i+1]):
                count+=1
        else:
                temp+=s[i]
                c=str(count)
                temp+=c
                count=1
if(s[n-2]!=s[n-1]):
    temp+=s[n-1]
    c=str(count)
    temp+=c
else:
    temp+=s[n-1]
    c=str(count)
    temp+=c
print temp
