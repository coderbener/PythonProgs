'''
a="Benhur"
print(a.lower())
'''
a="benhurSANthOSH"
i=0
b=""
while(i<len(a)):
    if(a[i].islower()):
        b+=a[i]
    else:
        b+=a[i].lower()
    i+=1
print(b)