a="anagram"
t="nagaram"
def anagram(a,t):
    sa=sorted(a)
    st=sorted(t)
    i=0
    count=0
    while(i<len(sa)):
        if(len(sa)==len(st)):
            if sa[i]!=st[i]:
                return False
            else:
                count+=1
            if(count==len(sa)):
                return True
        else:
            return False
        i+=1
    
print(anagram(a,t))
