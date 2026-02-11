class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        divisor = min(nums)

        remainder = max_num % divisor
        if remainder == 0:
            return divisor
        while remainder > 0:
            temp = remainder
            remainder = divisor % remainder
            divisor = temp
        return divisor
        