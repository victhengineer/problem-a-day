class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        size = len(arr)
        peak = 0

        if size < 3:
            return False

        for index in range(1, size):
            if arr[index - 1] >= arr[index]:
                break
            peak = index
        
        if peak == size - 1 or peak == 0:
            return False
        
        for idx in range(peak + 1, size):
            if arr[idx] >= arr[idx - 1]:
                return False
        
        return True

        