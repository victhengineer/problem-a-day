class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        seen_add = seen.add
        for num in nums:
            if num in seen:
                return True
            seen_add(num)
        return False