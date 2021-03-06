class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dit = {}
        for i, num in enumerate(nums):
            if target - num in dit:
                return [dit[target-num], i]
            dit[num] = i
        return []