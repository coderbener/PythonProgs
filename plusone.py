n=[123]
a=0
i=0
ln=len(n)
print(ln)
while(i<ln):
    if(i!=ln):
        a+=n[i]
        a*=10
    i+=1
a=a//10
s=a+1

st=str(s)

nums=[int(i) for i in st]
print(nums)