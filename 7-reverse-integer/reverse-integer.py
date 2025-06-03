class Solution(object):
    def reverse(self, x):
        x = str(x)
        if x[0] == '-':
            x = x[1:]
            x = x[::-1]
            x = int(x)
            if x >= (-1*(2**31)) and x < (2**31):
                return (-1)*x
            else:
                return 0
        else:
            x = x[::-1]
            x = int(x)
            if x >= (-(2**31)) and x < (2**31):
                return x
            else:
                return 0