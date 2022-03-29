class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for a in range(len(nums)):
            diff = target-nums[a]
            if diff in d:
                return [d[diff], a]
            d[nums[a]] = a
        
        
        