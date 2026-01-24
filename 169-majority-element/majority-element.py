class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        majority = nums[0]
        max_count = 1
        count = 1

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count > max_count:
                max_count = count
                majority = nums[i]
        return majority
        