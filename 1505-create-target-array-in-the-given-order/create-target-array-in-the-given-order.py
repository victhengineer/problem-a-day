class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []
        size = len(nums)

        for idx in range(size):
            target.insert(index[idx], nums[idx])
        return target
        