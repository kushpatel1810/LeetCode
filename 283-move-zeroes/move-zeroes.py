# class Solution:
#     def moveZeroes(self, num: List[int]) -> None:
#         for i in range(len(num)):
#             if num[i]==0:
#                 num[i]='A'
#                 num.append(0)
#         a='A'
#         while a in num:
#             num.remove(a)
              


class Solution:
    def moveZeroes(self, num: List[int]) -> None:
        for i in num:
            if i==0:
                num.remove(i)
                num.append(0)