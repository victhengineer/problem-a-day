class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lower_bound = 0
        upper_bound = len(nums) - 1

        while lower_bound <= upper_bound:
            midpoint = (upper_bound + lower_bound) // 2
            value_at_midpoint = nums[midpoint]

            if value_at_midpoint == target:
                return midpoint
            elif target < value_at_midpoint:
                upper_bound = midpoint - 1
            elif target > value_at_midpoint:
                lower_bound = midpoint + 1
        return -1
        