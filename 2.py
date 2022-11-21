str1=input()
str2=input()
l=str2[-1]
c=0
for i in str1:
    if(i==l):
        c+=1
print(c)