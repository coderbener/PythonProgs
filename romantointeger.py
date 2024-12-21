class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hm={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res=0
        i=0
        while(i<len(s)):
            if i<len(s)-1 and hm[s[i]]<hm[s[i+1]]:
                res+=hm[s[i+1]]-hm[s[i]]
                i+=2

            else:
                res+=hm[s[i]]
                i+=1
        return(res)
'''
left side velth aanel just add otherwise i+1-[i] 
MC aanel add M,
CM aanel c is less than m so M-C and inc by 2 pos
'''