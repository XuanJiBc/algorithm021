class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in itertools.permutations(nums, len(nums)):
            res.append(list(i))
        return res 