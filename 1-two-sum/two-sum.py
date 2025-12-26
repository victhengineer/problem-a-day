class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Iterate over the whole list
        for i in range(len(nums)):
            sum = 0
            # Skip the current index and iterate over the rest
            for j in range(i + 1, len(nums)):
                # sum both current
                sum = nums[i] + nums[j]
                if sum == target:
                    # return indices if sum equals to target
                    return [i,j]
        