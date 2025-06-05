import re
class Solution(object):
    def isPalindrome(self, s):
        s = (re.sub('[^a-zA-Z0-9]', "", s)).lower()
        print(s)

        r = s[::-1]
        print(r)

        if s == r:
            return True
        else:
            return False