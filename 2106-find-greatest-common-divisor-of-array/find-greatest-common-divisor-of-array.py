class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        divisor = min(nums)

        remainder = max(nums) % divisor
        if remainder == 0:
            return divisor
        while remainder > 0:
            temp = remainder
            remainder = divisor % remainder
            divisor = temp
        return divisor
        