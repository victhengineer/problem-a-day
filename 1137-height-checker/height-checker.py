class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        count = 0
        size = len(heights)

        for i in range(size):
            if heights[i] != expected[i]:
                count += 1
        return count
        