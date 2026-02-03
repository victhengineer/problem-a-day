class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        pairs = 0

        for i in range(size):
            for j in range(i + 1, size):
                if nums[i] == nums[j]:
                    pairs += 1
        return pairs
        