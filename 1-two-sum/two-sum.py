class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i, num in enumerate(nums):
            c = target-num
            if c in dict:
                return [nums.index(c),i]
            dict[num]=i