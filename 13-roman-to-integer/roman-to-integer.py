class Solution(object):
    def romanToInt(self, s):
        # priority_order = ['M','D','C','L','X','V','I']
        rank = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        # rank = {char:i for i, char in enumerate(priority_order)}
        # print(rank)
        # s = list(s)
        sum = 0
        i=0
        if len(s) == 1:
            return rank[s[0]]
        while i < (len(s)-1):
            if rank[s[i]] >= rank[s[i+1]]:
                sum+=rank[s[i]]
                print(sum)
                i+=1
                if i == (len(s)-1):
                    sum+=rank[s[i]]
            else:
                sum+=(rank[s[i+1]]-rank[s[i]])
                print(sum)
                i+=2
                if i == (len(s)-1):
                    sum+=rank[s[i]]
                
        print(sum)
        return sum




        #     print(s[0])
        # print(rank)

        