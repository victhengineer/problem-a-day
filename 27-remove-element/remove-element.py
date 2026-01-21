class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        result = []
        
        for num in nums:
            if num != val:
                result.append(num)
        nums[:] = result
        return len(nums)