class Solution:
    def moveZeroes(self, num: List[int]) -> None:
        for i in range(len(num)):
            if num[i]==0:
                num[i]='A'
                num.append(0)
        a='A'
        while a in num:
            num.remove(a)
              