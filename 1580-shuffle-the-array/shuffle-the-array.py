class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        result = []
        read = n

        for i in range(n):
            result.append(nums[i])
            result.append(nums[read])
            read += 1
        return result
        