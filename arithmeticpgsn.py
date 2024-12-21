arr=[20,17,-18,-13,13,-14,-8,10,1,14,-19]
sar=sorted(arr,reverse=True)
ln=len(sar)
i=0
d=[]
flag=0
while(i<ln-1):
    d.append(sar[i]-sar[i+1])
    i+=1
j=0
print(d)
if(len(d)==1):
    flag=1
while(j<ln-2):
    
    if d[j]!=d[j+1]:
        flag=0
        break
    else:
        flag=1
    j+=1
if flag==1:
    print("AP")
else:
    print("Not Ap")

