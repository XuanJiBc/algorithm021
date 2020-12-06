class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = len(nums) - k
        nums[:] = nums[a:] + nums[:a]
        return nums