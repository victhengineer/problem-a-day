class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        sum = 0
        for idx in range(len(nums)):
            sum += nums[idx]
            result.append(sum)
        return result
        