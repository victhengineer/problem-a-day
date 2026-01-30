class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        for idx in range(len(nums)):
            ans.append(nums[nums[idx]])
        return ans
        