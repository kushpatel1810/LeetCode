class Solution(object):
    def isPalindrome(self, x):
        if x >=0 and x < (2**31):
            lst_s = []
            lst_r = []
            while x != 0:
                r = x%10
                x=x/10
                lst_s.insert(0,r)
                lst_r.append(r)
            if lst_s == lst_r:
                return True
            else:
                return False
        else:
            return False
            