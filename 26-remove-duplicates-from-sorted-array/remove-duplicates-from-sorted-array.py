class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        seen_add = seen.add
        result = []

        for num in nums:
            if num not in seen:
                seen_add(num)
                result.append(num)
        nums[:] = result
        return len(nums)
            
        