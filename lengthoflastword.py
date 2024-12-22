'''
a="  hell world  "
b=a.strip().split()
l=len(b)-1
print(len(b[l]))
'''
length=0
a="  hell world  "
i=len(a)-1
while(a[i]==" "):
    i-=1
while(i>=0 and a[i]!=" "):
    length+=1
    i-=1
print(length)