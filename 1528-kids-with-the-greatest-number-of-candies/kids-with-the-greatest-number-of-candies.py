class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        highest = max(candies)
        for candy in candies:
            total = candy + extraCandies
            if total >= highest:
                result.append(True)
            else:
                result.append(False)
        return result
        
            
        