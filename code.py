class Solution:
    def romanToInt(self, s: str) -> int:    
        rom={'O':0,'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
                 'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        c=0
        if s in rom:
            c=c+rom[s]
        else:
            for i in range(len(s)):
                if s[i:i+2] in rom:

                    c=c+rom[s[i:i+2]]
                    s=s.replace(s[i+1:i+2],'O')


                else:

                    c=c+rom[s[i]]    
        return(c)  
