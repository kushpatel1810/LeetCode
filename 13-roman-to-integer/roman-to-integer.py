class Solution(object):
    def romanToInt(self, s):
        rank = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        sum = 0
        i=0
        if len(s) == 1:
            return rank[s[0]]
        while i < (len(s)-1):
            if rank[s[i]] >= rank[s[i+1]]:
                sum+=rank[s[i]]
                i+=1
                if i == (len(s)-1):
                    sum+=rank[s[i]]
            else:
                sum+=(rank[s[i+1]]-rank[s[i]])
                i+=2
                if i == (len(s)-1):
                    sum+=rank[s[i]]
                
        return sum